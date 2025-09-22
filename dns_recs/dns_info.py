
# RDPIT - Is an active reconnaissance tool for penetration testers and security researchers.
# Designed by Fixitgearware Security Cybersecurity Team.
# This tool is able to ping assets of any kinds, size to determine if they are active or not.
# It also has a DNS record information gathering module, enabling users to gather DNS records of domains or IPs.
# Website: https://fixitgearware.com
# GitHub: https://github.com/fixitgearware

#------Code Description Section------#

# This part of the tool is responsible for DNS record information retrieval.
# It uses the python package `dnspython` and the module dns.resolver to resolve domain into IPs.
# To enable the record info lookup and information gathering easily.


import dns.resolver
import dns.reversename
import socket

def dns_info(target: str):
    
    is_ip = False
    try:
        socket.inet_aton(target)
        is_ip = True
    except socket.error:
        pass

    record_types = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT', 'SOA', 'SRV', 'PTR', 'CAA', 'NAPTR', 'DNSKEY', 'DS']

    for record_type in record_types:
        try:
            if is_ip and record_type == 'PTR':
                rev_name = dns.reversename.from_address(target)
                response = dns.resolver.resolve(rev_name, 'PTR')
            elif is_ip:
                continue
            else:
                response = dns.resolver.resolve(target, record_type)

            print(f"\n[*] {record_type} records for {target}:")
            for rdata in response:
                print(f"- {rdata.to_text()}")

        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout, dns.resolver.NoNameservers):
            print(f"[!] No {record_type} record for {target}")
        except Exception as e:
            print(f"[!] Error fetching {record_type} for {target}: {e}")


      
                    
                    





