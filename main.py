from validator import InputValidator

def main():
    target_ip = get_target_ip_address()
    get_the_port_range()
    run_scaner()
    display_scanning_results()


def display_scanning_results():
    """ #TODO:
    Display the results to the user, indicating which ports are open and which are closed.
    """
    pass


def run_scaner():
    """ TODO:
    Implement a port scanning logic that checks if a port is open or closed on the target host.
    TIP: use Python's socket library to establish a connection to the target IP and port
    """
    pass


def get_the_port_range():
    while True:
        target_ports = input("Enter ports to scan.\n 
                          " - You can provide list of ports like: 80,444,6723"
                          " - Or you can provide reange of ports to scan: 7-1000\n"
                          "Set ports to scan: ")
        if InputValidator.port_value_is_valid(target_ports):
            return target_ports
        print(f"Provided ports value is invaild\n")


def get_target_ip_address():
    while True:
        target_ip = input("Enter target IP addres for scan: ")
        if InputValidator.ip_address_is_valid(target_ip):
            return target_ip
        print(f"Wrong IP addres: {target_ip}\n")


if __name__ == '__main__':
    main()
