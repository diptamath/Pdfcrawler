
from urllib.parse import urljoin
import urllib.request as urllib2
import requests
from os import path
import sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("error: please install bs4 ")
    sys.exit(0)
main_url= 'http://www.testurl.com'
dwnpath= "C:/users/user/Desktop"
 resp = urllib2.urlopen(main_url )
soup = BeautifulSoup(resp.read())
links = soup.find_all( 'a' )
if len(links)==0:
        raise Exception('No links found on the webpage')
    n_pdfs= 0
    for link in links:
        if link['href'][-4:]=='.pdf':
            n_pdfs+= 1
            content= requests.get(urljoin(dwnpath, link['href']))
            if content.status_code==200 and content.headers['content-type']=='application/pdf':
                with open(path.join(dwnpath, link.text+'.pdf'), 'wb') as pdf:
                    pdf.write(content.content)
    if n_pdfs==0:
        raise Exception('No pdfs found on the page')
    print("{0} pdfs downloaded and saved in {1}".format(n_pdfs, dwnpath)
