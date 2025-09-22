# RDPIT - Is an active reconnaissance tool for penetration testers and security researchers.
# Designed by Fixitgearware Security Cybersecurity Team.
# This tool is able to ping assets of any kinds, size to determine if they are active or not.
# It also has a DNS record information gathering module, enabling users to gather DNS records of domains or IPs.
# Website: https://fixitgearware.com
# GitHub: https://github.com/fixitgearware

#------Code Description Section------#
# Loads the domains from a file if file path is provided. 
# This function cleans the domain input by removing unwanted characters and formatting it correctly.
# Calls the clean function from utils/utils.py to clean the domain input.



import os
from dns_recs.load_domains import load_domains_from_file # type: ignore
from utils.utils import clean_domain # type: ignore
  


def parse_input(domain_input):
    # Check if the input is a file path, load domains from the file and clean them off unwanted characters and format them correctly
    if os.path.isfile(domain_input):
        print(f"[*] Detected file input: {domain_input}")
        raw = load_domains_from_file(domain_input)
        return [clean_domain(d) for d in raw]
    
    # Statement to handle multiple domains or IP inputs, seperated by commas (,) or both domains and IPs all-together
    elif ',' in domain_input:
        print("[*] Detected multiple domains")
        return [clean_domain(domain) for domain in domain_input.split(',') if domain.strip()]
    
 
   
    # Statement to handle single domain input
    else:
        print("[*] Detected single domain")
        return [clean_domain(domain_input.strip())]
