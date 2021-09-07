"""
The purpose of this file is to get the top level domain of the website
for use in the whois linux command.

@author Travis Hill
"""
from tld import get_tld

def get_domain_name(url):
    return get_tld(url)

