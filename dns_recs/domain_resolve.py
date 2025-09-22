# RDPIT - Is an active reconnaissance tool for penetration testers and security researchers.
# Designed by Fixitgearware Security Cybersecurity Team.
# This tool is able to ping assets of any kinds, size to determine if they are active or not.
# It also has a DNS record information gathering module, enabling users to gather DNS records of domains or IPs.
# Website: https://fixitgearware.com
# GitHub: https://github.com/fixitgearware

#------Code Description Section------#
# This file contains the code for resolving domain names to IP addresses.
# returning the IP if the input or file contains a domain name.
# and returns hostname for IP addresses if the input or file contains an IP address.
# This is to enable the DNS-RECORD-TOOL to fetch and display DNS records


import socket


def resolve_target(target: str) -> str:
    """
    Resolves a domain or performs reverse DNS for an IP.
    Returns the IP (for domain) or hostname (for IP), or None if fails.
    """
    target = target.strip()
   
    try:
        # Check if input is an IP
        socket.inet_aton(target)
        # If valid IP, do reverse lookup
        try:
            hostname = socket.gethostbyaddr(target)[0]
            print(f"[*] Reverse DNS: {target} → {hostname}")
            return hostname
        except socket.herror:
            print(f"[!] Reverse DNS lookup failed for IP {target}")
            return target
    except socket.error:
        # Not an IP, assume domain
        try:
            ip = socket.gethostbyname(target)
            print(f"[*] {target} resolves to IP: {ip}")
            return target  # still return domain for DNS record lookups
        except socket.gaierror:
            print(f"[!] Could not resolve domain: {target}")
            return None


    



