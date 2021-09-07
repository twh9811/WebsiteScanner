"""
The purpose of this file is to take the ipAddress and run it through an nMap scan.
Gathering which ports are open on the webserver in the process.

@author Travis Hill
"""
import os

def scanNMap(settings, ipAddress):
    command = "nmap " + settings + " " + ipAddress
    process = os.popen(command)
    results = str(process.read())
    return results