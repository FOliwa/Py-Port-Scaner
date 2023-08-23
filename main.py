def main():
    get_target_IP_address()
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
    """ TODO:
    Ask the user for a range of ports to scan. 
    You can choose to scan a specific range (e.g., 1-1000) or provide a list of common ports to scan.
    """
    pass


def get_target_IP_address():
    """ #TODO:
    Prompt the user to enter a target IP address or hostname to scan.
    """
    pass


if __name__ == '__main__':
    main()
