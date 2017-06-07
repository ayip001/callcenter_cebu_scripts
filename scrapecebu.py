# written by github.com/ayip001.

import re
import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer
import csv
import numbers

from secret_url import secret_url
from param import param

def parse_url(month, day, param):
    http = httplib2.Http()
    status, response = http.request(secret_url["URL"] +
        'bioleans_inbound-tl/?action=searchByDate&day=' + day +
        '&dispo=&phone_number=&month=' + month)
    return BeautifulSoup(response, parseOnlyThese=SoupStrainer(param))

def find_names(month, day):
    names = []
    for line in parse_url(month, day, 'td'):
        m = re.search('<td>\D+<\/td>', str(line))
        if m:
            names.append(str(line).split('<td>')[1].split('</td>')[0])
    return names[9:]

def find_num_names(month, day, minCalls):
    if len(day) == 1:
        day = '0' + day
    num_names = []
    for element in find_names(month, day):
        if num_names.count(element) == 0:
            num_names.extend([element, 1])
        else:
            num_names[num_names.index(element) + 1] += 1
    # return num_names # in the format of ['name1', #calls, 'name2', #calls] etc
    total = 0
    for element in num_names:
        if isinstance(element, numbers.Number) and element >= minCalls:
            total += 1
    return total

def generate_csv():
    with open(param['START_DATE'] + '_' + param['END_DATE'] + '.csv', 'wb') \
        as csvfile:
        w = csv.writer(csvfile, delimiter=',', quoting = csv.QUOTE_NONE)
        for num in range(int(param['START_DATE'].split('-')[1]),
                         int(param['END_DATE'].split('-')[1]) + 1):
            w.writerow([param['START_DATE'].split('-')[0] + '-' + str(num),
                       str(find_num_names(param['START_DATE'].split('-')[0],
                       str(num), param['MIN_NUM_CALLS']))])


def find_total_time(month, day):
    totalTime = 0;
    for link in parse_url(month, day, 'a'):
        m = re.search('\((.+?)\sm', str(link))
        if m:
            totalTime += float(m.group(1))
        # if link.has_key('href'):
        #     print link['href']
    return totalTime
