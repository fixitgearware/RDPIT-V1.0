# RDPIT - Is an active reconnaissance tool for penetration testers and security researchers.
# Designed by Fixitgearware Security Cybersecurity Team.
# This tool is able to ping assets of any kinds, size to determine if they are active or not.
# It also has a DNS record information gathering module, enabling users to gather DNS records of domains or IPs.
# Website: https://fixitgearware.com
# GitHub: https://github.com/fixitgearware

#------Code Description Section------#

# This module provides functionality to load domain names from a specified file.
# when the user serves a file containing domain names, this module reads the file and returns a list of domains.
# Throws an error message if the file is not found or file path is incorrect.


import os
from typing import List


def load_domains_from_file(file_path: str) -> List[str]:
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] File not found: {file_path}")
        return []

