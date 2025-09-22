# RDPIT - Is an active reconnaissance tool for penetration testers and security researchers.
# Designed by Fixitgearware Security Cybersecurity Team.
# This tool is able to ping assets of any kinds, size to determine if they are active or not.
# It also has a DNS record information gathering module, enabling users to gather DNS records of domains or IPs.
# Website: https://fixitgearware.com
# GitHub: https://github.com/fixitgearware

#------Code Description Section------#
# This file contains constants used throughout the RDPIT tool.
# These constants include file names for storing reachable and unreachable IP addresses.
# Constants called to create files that stores and append to the files Ip addresses or domains 
# that are reachable and unreachable. for each ping request results are appended to the files.

IP_REACHABLE_FILE = "reachable_ips.txt"
IP_UNREACHABLE_FILE = "unreachable_ips.txt"
