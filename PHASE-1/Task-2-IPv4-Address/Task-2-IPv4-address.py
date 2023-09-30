import re
def validate_the_ipv4_address(IP):
    # Regular expression pattern to check a valid IPv4 address...
    __pattern__ = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'

    # Check if the input is also same as the pattern....
    if re.match(__pattern__, IP):
        # Split the IP address into its four parts
        parts = IP.split('.')
        for part in parts:
            # Check if each part is within the valid range (0-255)....
            if not (0 <= int(part) <= 255):
                return False
        return True
    else:
        return False

# Input an IPv4 address to check the given IPv4 address is also same or not
ip_address = input("Enter an IPv4 address: ")

# Validate the input
if validate_the_ipv4_address(ip_address):
    print(f"{ip_address} is a valid IPv4 address.")
else:
    print(f"{ip_address} is not a valid IPv4 address.")
