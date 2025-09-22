# RDPIT - Is an active reconnaissance tool for penetration testers and security researchers.
# Designed by Fixitgearware Security Cybersecurity Team.
# This tool is able to ping assets of any kinds, size to determine if they are active or not.
# It also has a DNS record information gathering module, enabling users to gather DNS records of domains or IPs.
# Website: https://fixitgearware.com
# GitHub: https://github.com/fixitgearware

#------Code Description Section------#
# creates a file if it doesn't exist and logs the reachable and unreachable IP addresses to separate files.
# these files can be used for further analysis such as vulnerability scanning using tools like nmap, nessus, openvas, etc.
# Or resolve the dns records using the dns option in this tool.

from utils.constants import IP_REACHABLE_FILE, IP_UNREACHABLE_FILE #importing the constants from the utils/constants.py file

def log_result(ip, reachable):
    filename = IP_REACHABLE_FILE if reachable else IP_UNREACHABLE_FILE
    with open(filename, 'a') as f:
        f.write(f"{ip}\n") # Append the IP address to the file in a new line. 
        
