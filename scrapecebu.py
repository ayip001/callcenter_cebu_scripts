import re
import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer

from secret_url import secret_url

http = httplib2.Http()
status, response = http.request(secret_url["URL"])

def find_names():
    for line in BeautifulSoup(response, parseOnlyThese=SoupStrainer('td')):
        m = re.search('<td>\D+<\/td>', str(line))
        if m:
            print str(line).split('<td>')[1].split('</td>')[0]

def find_total_time():
    totalTime = 0;
    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
        m = re.search('\((.+?)\sm', str(link))
        if m:
            totalTime += float(m.group(1))
        # if link.has_key('href'):
        #     print link['href']
    print totalTime
