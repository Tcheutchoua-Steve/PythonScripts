#import urllib.request
import urllib
#from bs4 import BeautifulSoup
from BeautifulSoup import *
url = raw_input('Please provide the url  - ')
#url = input('Enter - ')
#html = urllib.request.urlopen(url).read()
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)


# Each tag is like a dictionary of HTML attributes

tags = soup.findAll('h4')

for tag in tags :
    print tag
