class InputValidator:

    @staticmethod
    def ip_address_is_valid(ip_addr: str) -> bool:
        try:
            return all(map(lambda x: x.isdigit(), ip_addr.split('.')))
        except Exception:
            return False

    @staticmethod
    def port_value_is_valid(port: str) -> bool:
        