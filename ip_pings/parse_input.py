# RDPIT - Is an active reconnaissance tool for penetration testers and security researchers.
# Designed by Fixitgearware Security Cybersecurity Team.
# This tool is able to ping assets of any kinds, size to determine if they are active or not.
# It also has a DNS record information gathering module, enabling users to gather DNS records of domains or IPs.
# Website: https://fixitgearware.com
# GitHub: https://github.com/fixitgearware

#------Code Description Section------#
# Passes user input to determine if it's a single IP, multiple IPs, or a file containing IPs.
# Calls the appropriate function to handle the input and returns a list of IPs. e.g. single IP, multiple IPs, or file path.





import os
from ip_pings.load_ips import load_ips_from_file # Function to load IPs from a file or file paths provided by the user.

def parse_input(ip_input:str):
    ip_input = ip_input.strip() # Remove leading/trailing whitespace from the input.
    if os.path.isfile(ip_input):
        print(f"Detected file input: {ip_input}") # Check if the input is a file path, and detect the file.
        return load_ips_from_file(ip_input)
    elif ',' in ip_input: # Check if the input contains commas, indicating multiple IPs.
        print("Detected multiple IPs")
        return [ip.strip() for ip in ip_input.split(',') if ip.strip()] # Split the input by commas and strip whitespace, ensuring no empty strings are included.
    else:
        print("Detected single IP") #check if the input is a single IP address.
        return [ip_input.strip()]
