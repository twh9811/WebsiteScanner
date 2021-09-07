"""
The purpose of this file is to take the an ip address and run it through an nMap scan.
Gathering which ports are open on the webserver in the process.

@author Travis Hill
"""
import subprocess

def scanNMap(settings, ipAddress):
    process = subprocess.run(["nmap", settings, ipAddress], capture_output=True)
    results = process.stdout.decode()
    return results