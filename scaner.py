import socket
import threading
from more_itertools import chunked


class PortScaner:
    """
    Notes:
    - Implement scaning logic here - use Python socket lib
    - A listening socket does just what its name suggests. It listens for connections from clients.
    - The client calls .connect() to establish a connection to the server and initiate the three-way handshake. 
    """
    def __init__(self, target_hosts=["127.0.0.1"], target_ports: [list, range] = [80]) -> None:
        self.debug = False
        self.target_hosts = target_hosts
        self.target_ports = target_ports
        self.results = {}
        self.scan_tcp = True
        self.scan_udp = True

    def run_scanner(self):

        for host in self.target_hosts:
            self.results[host] = {"open_tcp_ports": [],
                                  "open_udp_ports": []}
            if self.scan_tcp:
                for port in self.target_ports:
                    self.tcp_port_open(host, port)

            if self.scan_udp:
                threads = []
                chunk_size = int(len(self.target_ports)/10)
                for ports_chunk in chunked(self.target_ports, chunk_size):
                    thread = threading.Thread(target=self.udp_port_open, args=(host, ports_chunk))
                    thread.start()
                    threads.append(thread)

                for thread in threads:
                    thread.join()

    def tcp_port_open(self, target_host, target_port):
        """ Scan TCP port by establish connection between targeted system on 
        defined port. If connection established - it means the port is open.
        """
        try:
            # Try to establish connection
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_client:
                tcp_client.connect((target_host, target_port))
                if self.debug:
                    print(f"Connection to {target_host}:{target_port} is established!")
                self.results["open_tcp_ports"].append(target_port)
        except socket.timeout:
            if self.debug:
                print(f"Port {target_port} is closed (timeout)")
        except ConnectionRefusedError:
            if self.debug:
                print(f"Port {target_port} is closed (connection refused)")
        except Exception as e:
            if self.debug:
                print(f"Connection to {target_host}:{target_port} failed: {e}")

    def udp_port_open(self, target_host, target_ports):
        """ Scanning UDP ports required diffrent approach than scaning TCP ports becouse
        there is no "connection" to establish. Thats why I have to realy on recieiving some
        response from saning port of targeted system.
        """
        print(f"Start Thread for ports: {target_ports}")
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_client:
            # Timeout for reciving reponses
            # Scaning UDP take much more time then TCP
            udp_client.settimeout(1)
            for port in target_ports:
                try:
                    udp_client.sendto(b"Hello!", (target_host, port))
                    response, _ = udp_client.recvfrom(1024)
                    if self.debug:
                        print(f"UDP Port {port} is open")
                    self.results["open_udp_ports"].append(port)
                except socket.timeout:
                    """
                    Analyzing response in UDP case is not so obvius like in TCP case
                    If you don't receive any response (timeout), the port's state is uncertain.
                    Some options is such case are:
                    - retry mechanism
                    - multiple scans
                    - scan commonly use ports (specific for knonw services)
                    - if port is TCP you dont need UDP scan on it then
                    """
                    if self.debug:
                        print(f"Timeout: UDP Port {port} state is uncertain - most probably filtered or closed")
                except Exception as e:
                    if self.debug:
                        print(f"Error scaning UDP Port {port}: {e}")

    def display_scanning_results(self):
        for host, ports in self.results.items():
            print("_" * 40)
            print(f"Open ports for host: {host}:")
            print(type(ports))
            print(ports)
            if self.scan_tcp:
                open_tcp_ports = ports['open_tcp_ports']
                print(f"Open TCP ports:\n\t {open_tcp_ports}\n")
            if self.scan_udp:
                open_udp_ports = ports['open_udp_ports']
                print(f"Open UDP ports:\n\t {open_udp_ports}\n")
            if not any([self.scan_tcp, self.scan_udp]):
                print("Nothing to scann - select TCP or UDP port scaning.\n")
