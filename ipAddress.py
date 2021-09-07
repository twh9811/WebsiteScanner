"""
The purpose of this file is to obtain the websites IP address
using the host command in Linux

@author Travis Hill
"""
import os

def get_ip_address(url):
    command = 'host ' + url
    process = os.popen(command)
    results = str(process.read())
    splitResults = results.split(" ")
    return splitResults[3]