import socket


class PortScaner:
    """
    Notes:
    - Implement scaning logic here - use Python socket lib
    - A listening socket does just what its name suggests. It listens for connections from clients.
    - The client calls .connect() to establish a connection to the server and initiate the three-way handshake. 
    """
    def start_scan(self, target_host="127.0.0.1", target_port=80):
        try:
            # Create socket obj using with and close at the end
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                # Try to connect
                client.connect((target_host, target_port))
                print(f"Connection to {target_host}:{target_port} is established!")
        except Exception as e:
            print(f"Connection to {target_host}:{target_port} failed: {e}")
