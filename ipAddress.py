"""
The purpose of this file is to obtain a websites IP address using the host command in Linux

@author Travis Hill
"""
import subprocess

def get_ip_address(domainName):
    process = subprocess.run(["host", domainName], capture_output=True)
    results = process.stdout.decode()
    splitResults = results.split(" ")
    return splitResults[3].splitlines()[0]