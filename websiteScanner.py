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

def writeFile(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()

def generateReport(name, url, domainName, nmap, robotsTxt, whois):
    path = input("Please enter where you want to store your file... ")
    writeFile(path + "url.txt", url)
    writeFile(path + "domainName.txt", domainName)
    writeFile(path + "nmap.txt", nmap)
    writeFile(path + "robots.txt", robotsTxt)
    writeFile(path + "whois.txt", whois)

def scanWebsite(name, url):
    domainName = get_domain_name(url)
    websiteIP = get_ip_address(url)
    nMap = scanNMap("-F", websiteIP)
    robotFile = getRobotsTxt(url)
    whoisScan = get_whois(url)
    generateReport(name, url, domainName, nMap, robotFile, whoisScan)
