"""
The purpose of this file is to get the robots.txt file some websites have.
This gives the user more information about the website if they wish to scrape it.

@author Travis Hill
"""
import urllib.request
import io

def getRobotsTxt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + "/"
    req = urllib.request.urlopen(path + "robots.txt", data=None)
    data = io.TextIOWrapper(req, encoding='utf-8')
    return data.read()