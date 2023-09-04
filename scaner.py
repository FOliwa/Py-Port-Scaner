import socket


class PortScaner:
    """
    Notes:
    - Implement scaning logic here - use Python socket lib
    - A listening socket does just what its name suggests. It listens for connections from clients.
    - The client calls .connect() to establish a connection to the server and initiate the three-way handshake. 
    """
    def __init__(self, target_hosts=["127.0.0.1"], target_ports: [list, range] = [80]) -> None:
        self.target_hosts = target_hosts
        self.target_ports = target_ports
        self.open_tcp_ports = []
        self.open_upd_ports = []
        self.scan_tcp = True
        self.scan_udp = False

    def run_scanner(self):
        # TODO: Find better way to scan it - split scaning to multiple threads

        for host in self.target_hosts:
            if self.scan_tcp:
                self.open_tcp_ports = [port for port in self.target_ports if self.tcp_port_open(host, port)]
                # print(f"Open TCP ports for host: {host}:")
                # print(f"{open_tcp_ports}")

            if self.scan_udp:
                self.open_upd_ports = [port for port in self.target_ports if self.udp_port_open(host, port)]
                # print(f"Open UDP ports for host: {host}:")
                # print(f"{open_udp_ports}")


    def tcp_port_open(self, target_host, target_port):
        """ Scan TCP port by establish connection between targeted system on 
        defined port. If connection established - it means the port is open.
        """
        try:
            # Try to establish connection
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_client:
                tcp_client.connect((target_host, target_port))
                print(f"Connection to {target_host}:{target_port} is established!")
                return True
        except socket.timeout:
            pass
            # print(f"Port {target_port} is closed (timeout)")
        except ConnectionRefusedError:
            pass
            # print(f"Port {target_port} is closed (connection refused)")
        except Exception as e:
            pass
            # print(f"Connection to {target_host}:{target_port} failed: {e}")
        return False

    def udp_port_open(self, target_host, target_port):
        """ Scanning UDP ports required diffrent approach than scaning TCP ports becouse
        there is no "connection" to establish. Thats why I have to realy on recieiving some
        response from saning port of targeted system.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_client:
            # Timeout for reciving reponses
            # Scaning UDP take much more time then TCP
            udp_client.settimeout(1)
            try:
                udp_client.sendto(b"Hello!", (target_host, target_port))
                response, _ = udp_client.recvfrom(1024)
                print(f"UDP Port {target_port} is open")
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
                print(f"Timeout: UDP Port {target_port} state is uncertain - most probably filtered or closed")
            except Exception as e:
                print(f"Error scaning UDP Port {target_port}: {e}")
        return False

    def display_scanning_results(self):
        print(f"Open ports for host: {self.target_hosts}:")
        if self.scan_tcp:
            print(f"Open TCP ports for host: {self.open_tcp_ports}:")
        if self.scan_udp:
            print(f"Open TCP ports for host: {self.open_upd_ports}:")
        if any([self.scan_tcp, self.scan_udp]):
            print("Nothing to scann - select TCP or UDP port scaning.")
