# RDPIT - Is an active reconnaissance tool for penetration testers and security researchers.
# Designed by Fixitgearware Security Cybersecurity Team.
# This tool is able to ping assets of any kinds, size to determine if they are active or not.
# It also has a DNS record information gathering module, enabling users to gather DNS records of domains or IPs.
# Website: https://fixitgearware.com
# GitHub: https://github.com/fixitgearware

#------Code Description Section------#
# This module contains utility functions for the RDPIT tool.
# It includes functions for cleaning and validating domain names.
# The clean_domain function processes a given domain or URL to extract and return a standardized domain name.

import re
from urllib.parse import urlparse


def clean_domain(domain):
    # Remove any leading or trailing whitespace
    domain = domain.strip()
    url_pattern = "://"

    # If it's a full URL, parse it
    if url_pattern in domain:
        parsed = urlparse(domain)
        domain = parsed.netloc
    else:
        # Removes any slashes or paths manually
        domain = domain.split('/')[0]

    # Removes www. and empty spaces if present at the beginning of the domain or domain list provided by the user.
    domain = re.sub(r'^www\.', '', domain)

    return domain.lower() # Convert all domain provided or in the domain list provided to lowercase for consistency. 
