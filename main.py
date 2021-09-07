"""
The purpose of this file is to run the website scanner and generate a report.

@author Travis Hill
"""
from websiteScanner import *

def main():
    name = input("Please enter the website name: ")
    url = input("Please enter the website URL: ")
    scanWebsite(name, url)

main()
