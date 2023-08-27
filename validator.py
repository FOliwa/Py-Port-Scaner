import re


class InputSanitizer:

    @staticmethod
    def sanitize_provided_ip_value(ip_addr: str):
        try:
            ip_components = ip_addr.split('.')
            if len(ip_components) == 4 and all(map(lambda x: x.isdigit(), ip_components)):
                return ip_addr
        except Exception:
            return False

    @staticmethod
    def sanitize_provided_ports_value(ports_value: str):
        range_pattern = r"(\d+)-(\d+)"
        match = re.match(range_pattern, ports_value)
        try:
            if match:
                start_value = int(match.group(1))
                end_value = int(match.group(2))
                return range(start_value, end_value) if start_value < end_value else False
            else:
                ports = ports_value.split(',')
                if all([p.isdigit() for p in ports]):
                    return map(int, [p for p in ports if p.isdigit()])
        except Exception:
            return False
