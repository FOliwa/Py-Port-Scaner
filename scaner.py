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

    def run_scanner(self):
        # TODO: Find better way to scan it - split scaning to multiple threads
        open_ports = []

        for host in self.target_hosts:
            open_ports = [port for port in self.target_ports if self.tcp_port_open(host, port)]
            print(f"List of open ports for host: {host}:")
            print(f"{open_ports}")
                    

    def tcp_port_open(self, target_host, target_port):
        try:
            # Try to establish connection
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect((target_host, target_port))
                print(f"Connection to {target_host}:{target_port} is established!")
                return True
        except socket.timeout:
            print(f"Port {target_port} is closed (timeout)")
        except ConnectionRefusedError:
            print(f"Port {target_port} is closed (connection refused)")
        except Exception as e:
            print(f"Connection to {target_host}:{target_port} failed: {e}")
        return False

    def scan_udp_port():
        pass
