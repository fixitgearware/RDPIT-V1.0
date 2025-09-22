# RDPIT - Is an active reconnaissance tool for penetration testers and security researchers.
# Designed by Fixitgearware Security Cybersecurity Team.
# Website: https://fixitgearware.com
# GitHub: https://github.com/fixitgearware
# This tool is able to ping assets of any kinds, size to determine if they are active or not.
# It also has a DNS record information gathering module, enabling users to gather DNS records of domains or IPs.

#------Code Description Section------#
# This is the main script that provides a command-line interface for users to choose between pinging IPs
# or resolving DNS records. It handles user input, calls the appropriate functions from other modules,
# and displays the results.





import signal # For handling Ctrl+C gracefully
from ip_pings.parse_input import parse_input as parse_ip_input # Function to parse IP input
from ip_pings.ping_ip import ping_ip # Function to ping an IP address
from ip_pings.log_result import log_result # Function to log ping results
from utils.signal_handler import signal_handler # Custom signal handler for graceful exit on Ctrl+C
from dns_recs.resolver import resolve_target # Function to resolve domain or IP depending on input or content type in file. 
from dns_recs.dns_info import dns_info # Function to gather and display DNS records that can be obtained via DNS queries.
from dns_recs.load_domains import load_domains_from_file # Function to load domains from a file. 
import os # For file path checks in the operating system when the file path is provided.
import sys

signal.signal(signal.SIGINT, signal_handler)

rdpit_banner = r"""

 /$$$$$$$  /$$$$$$$  /$$$$$$$  /$$$$$$ /$$$$$$$$
| $$__  $$| $$__  $$| $$__  $$|_  $$_/|__  $$__/
| $$  \ $$| $$  \ $$| $$  \ $$  | $$     | $$   
| $$$$$$$/| $$  | $$| $$$$$$$/  | $$     | $$   
| $$__  $$| $$  | $$| $$____/   | $$     | $$   
| $$  \ $$| $$  | $$| $$        | $$     | $$   
| $$  | $$| $$$$$$$/| $$       /$$$$$$   | $$   
|__/  |__/|_______/ |__/      |______/   |__/   
                                                                                                
"""
print(rdpit_banner)


def run_ping():
    print("\n=== Ping Mode ===")
    ip_input = input("Enter IP or IPs seperated by (,) or file path: ").strip()
    if not ip_input:
        print("[!] No input provided.")
        return

    ip_list = parse_ip_input(ip_input)
    for ip in ip_list:
        if not ip:
            print(f"[!] Invalid IP, skipping: '{ip}'")
            continue
        print(f"Pinging {ip}...")
        response = ping_ip(ip)
        if response is not None:
            print(f" ✅ {ip} is reachable. Response time: {response*1000:.2f} ms")
            log_result(ip, True)
        else:
            print(f" ⚠️  {ip} is not reachable.")
            log_result(ip, False)
    print("\nIP results logged. Check the file 'reachable_ips.txt' for valid IPs and 'unreachable_ips.txt' for inactive IPs.")

def run_dns():
    print("\n=== DNS Mode ===")
    domain_input = input("Enter domain(s), IP(s), or file path: ").strip()
    if not domain_input:
        print("[!] No input provided.")
        return

    if os.path.isfile(domain_input):
        targets = load_domains_from_file(domain_input)
    elif ',' in domain_input:
        targets = [t.strip() for t in domain_input.split(',') if t.strip()]
    else:
        targets = [domain_input]

    for target in targets:
        resolved_target = resolve_target(target)
        if not resolved_target:
            continue
        print(f"\n=== DNS Info for {resolved_target} ===")
        dns_info(resolved_target)
        print("="*40)

def main_menu():
    print("\n=== An Active Recon Tool For Cybersecurity Professionals ===")
    print("\n")
    while True:
        choice = input("Do you want to ping IPs or resolve DNS records? (Enter 'ping', 'dns', 'exit'): ").strip().lower()
        if choice == 'ping':
            run_ping()
        elif choice == 'dns':
            run_dns()
        elif choice == 'exit':
            print("Exiting...")
            break
        else:
            print("[!] Invalid choice. Enter 'ping', 'dns', or 'exit'.")

if __name__ == "__main__":
    main_menu()
