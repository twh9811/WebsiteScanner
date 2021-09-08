"""
The purpose of this file is to run the website scanner and generate a report.

@author Travis Hill
"""
from websiteScanner import *

def main():
    name = input("Please enter the website name: ")
    url = input("Please enter the website URL: ")
    ipAns = input("Do you want multiple IPs to be recorded? (Y/N): ")
    if ipAns.upper() == "Y":
        scanWebsite(name, url, True)
    else:
        scanWebsite(name, url)

main()
