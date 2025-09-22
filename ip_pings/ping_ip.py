# RDPIT - Is an active reconnaissance tool for penetration testers and security researchers.
# Designed by Fixitgearware Security Cybersecurity Team.
# This tool is able to ping assets of any kinds, size to determine if they are active or not.
# It also has a DNS record information gathering module, enabling users to gather DNS records of domains or IPs.
# Website: https://fixitgearware.com
# GitHub: https://github.com/fixitgearware

#------Code Description Section------#
# This code is a part of the RDPIT tool, specifically for pinging IP addresses to check their availability.
# It uses the ping3 library to send ICMP echo requests to the specified IP address and returns the response time.
# If the ping is successful, it returns the response time; otherwise, it handles exceptions and prints an error message.


import ping3 # type: ignore
import time

def ping_ip(ip:str):  #function to ping an IP address from the input provided by the user. 
    try:
        response = ping3.ping(ip, timeout=2)
        time.sleep(1)
        return response
    except Exception as e:
        print(f"There is an error pinging {ip}: {e}") #print the error message if there is an error pinging the IP address.
        return None
