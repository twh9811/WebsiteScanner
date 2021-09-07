"""
The purpose of this file is to run the whois command on linux
The URL must be the domain name only.

@author Travis Hill
"""
import subprocess

def get_whois(url):
    process = subprocess.run(['whois', url], capture_output=True)
    results = process.stdout.decode()
    return results