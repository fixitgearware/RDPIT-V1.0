# RDPIT - Is an active reconnaissance tool for penetration testers and security researchers.
# Designed by Fixitgearware Security Cybersecurity Team.
# This tool is able to ping assets of any kinds, size to determine if they are active or not.
# It also has a DNS record information gathering module, enabling users to gather DNS records of domains or IPs.
# Website: https://fixitgearware.com
# GitHub: https://github.com/fixitgearware

#------Code Description Section------#
# This file contains the signal handler to gracefully handle interruptions like Ctrl+C. from the user. 
# This closes everything and that includes current actions being carried out, and exits the program without any errors.



import sys

def signal_handler(sig, frame):
    print("\nProcess interrupted. Program will now Exit...")
    sys.exit(0)
