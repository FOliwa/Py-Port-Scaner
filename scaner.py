import socket


class PortScaner:
    """
    Notes:
    - Implement scaning logic here - use Python socket lib
    - A listening socket does just what its name suggests. It listens for connections from clients.
    - The client calls .connect() to establish a connection to the server and initiate the three-way handshake. 
    """
    def __init__(self, target_hosts=["127.0.0.1"], target_ports=[80]) -> None:
        self.target_hosts = target_hosts
        self.target_ports = target_ports

    def run_scanner(self):
        for host in self.target_hosts:
            for port in self.target_ports:
                self.scan(host, port)

    def scan(self, target_host, target_port):
        try:
            # Create socket obj using with and close at the end
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                # Try to connect
                client.connect((target_host, target_port))
                print(f"Connection to {target_host}:{target_port} is established!")
        except Exception as e:
            print(f"Connection to {target_host}:{target_port} failed: {e}")
