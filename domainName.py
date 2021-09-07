"""
The purpose of this file is to get the top level domain of the website.

@author Travis Hill
"""
from tld import get_fld

def get_domain_name(url):
    return get_fld(url)

