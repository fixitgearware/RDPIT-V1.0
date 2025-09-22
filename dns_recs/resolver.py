# RDPIT - Is an active reconnaissance tool for penetration testers and security researchers.
# Designed by Fixitgearware Security Cybersecurity Team.
# This tool is able to ping assets of any kinds, size to determine if they are active or not.
# It also has a DNS record information gathering module, enabling users to gather DNS records of domains or IPs.
# Website: https://fixitgearware.com
# GitHub: https://github.com/fixitgearware

#------Code Description Section------#
#resolver.py: This module handles DNS resolution tasks, including resolving domain names to IP addresses 
# and performing reverse lookups for IP addresses.





import socket

def resolve_target(target: str) -> str:
    
    target = target.strip()
    try:
        #If it is an IP address provided? Check if it's a valid IP. If so, perform reverse lookup.
        socket.inet_aton(target)
        # Reverse lookup for IP
        try:
            hostname = socket.gethostbyaddr(target)[0]
            print(f"[*] Reverse DNS: {target} → {hostname}")
            return hostname
        except socket.herror:
            print(f"[!] Reverse DNS failed for IP {target}")
            return target
    except socket.error:
        # Assume domain
        try:
            ip = socket.gethostbyname(target)
            print(f"[*] {target} resolves to IP: {ip}")
            return target
        except socket.gaierror:
            print(f"[!] Could not resolve domain: {target}")
            return None
