# RDPIT - Is an active reconnaissance tool for penetration testers and security researchers.
# Designed by Fixitgearware Security Cybersecurity Team.
# This tool is able to ping assets of any kinds, size to determine if they are active or not.
# It also has a DNS record information gathering module, enabling users to gather DNS records of domains or IPs.
# Website: https://fixitgearware.com
# GitHub: https://github.com/fixitgearware

#------Code Description Section------#
# This module handles loading IP addresses from a file.
# It reads a file containing IP addresses, one per line, and returns them as a list.
# when the ping option is selected by the user, and the user provides a file path containing IPs.


def load_ips_from_file(file_path):   # Function to load IPs from a file or file paths provided by the user.
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError: # Handle the case where the file does not exist. 
        print(f"File not found: {file_path}")
        return []
