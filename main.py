from typing import List

from validator import InputSanitizer
from scaner import PortScaner


def main():
    ip_address = get_target_ip_address()
    ports = get_target_ports()
    scaner = PortScaner([ip_address], ports)
    scaner.run_scanner()
    scaner.display_scanning_results()


def get_target_ports() -> List[int]:
    while True:
        ports_value = input("Enter ports to scan.\n"
                            " - You can provide list of ports like: 80,444,6723\n"
                            " - Or you can provide reange of ports to scan: 7-1000\n"
                            "Set ports to scan: ")
        sanitized_ports = InputSanitizer.sanitize_provided_ports_value(ports_value)
        if sanitized_ports:
            return sanitized_ports
        print(f"Provided ports value is invaild\n")


def get_target_ip_address():
    while True:
        provided_ip = input("Enter target IP addres for scan: ")
        sanitize_ip = InputSanitizer.sanitize_provided_ip_value(provided_ip)
        if sanitize_ip:
            return sanitize_ip
        print(f"Wrong IP address format: {provided_ip}\n")


if __name__ == '__main__':
    main()
