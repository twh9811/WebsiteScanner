"""
The purpose of this file is to create a text file containing information about a website.

@author Travis Hill
"""
from ipAddress import get_ip_address
from domainName import *
from ipaddress import *
from nMap import *
from robotTxt import *
from whoIs import *
import os
import subprocess
ROOT_DIRECTORY = 'Desktop'
def writeFile(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()

def mkdir(name):
    if os.path.isdir(name):
        print("Directory already exists. Try a different name")
    else:
        subprocess.run(['mkdir', name])

def generateReport(name, url, domainName, nmap, robotsTxt, whois):
    # path = ROOT_DIRECTORY + "/" + name
    # mkdir(path)
    writeFile("url.txt", url)
    writeFile("domainName.txt", domainName)
    writeFile("nmap.txt", nmap)
    writeFile("robots.txt", robotsTxt)
    writeFile("whois.txt", whois)

def scanWebsite(name, url):
    domainName = get_domain_name(url)
    websiteIP = get_ip_address(url)
    nMap = scanNMap("-F", websiteIP)
    robotFile = getRobotsTxt(url)
    whoisScan = get_whois(url)
    generateReport(name, url, domainName, nMap, robotFile, whoisScan)
