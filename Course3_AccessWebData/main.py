import re
import socket
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import json

def exercise_1():
    output_lst = list()
    fopen = open('regex_sum_184184.txt')
    for line in fopen:
        line = line.rstrip()
        line_out = re.findall('[0-9]+',line)
        if len(line_out) == 0:
            continue
        for x in line_out:
            output_lst.append(x)
    output_lst = list(map(int, output_lst))
    return sum(output_lst)
#result = exercise_1()
#print(result)
def exercise_2():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')
    mysock.close()
#exercise_2()
def exercise_3():
    sum_value = 0
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    #url = input('Enter - ')
    url = 'http://py4e-data.dr-chuck.net/comments_184186.html'
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('span')
    for tag in tags:
        sum_value += int(tag.contents[0])
    print(sum_value)
#exercise_3()

def exercise_4():
    sum_value = 0
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    #url = input('Enter - ')
    url = 'http://py4e-data.dr-chuck.net/known_by_Sarah.html'
    for x in range(7):
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        # Retrieve all of the anchor tags
        tags = soup('a')
        url = tags[17].get('href', None)
        #print(url)
    start_pos = url.find('by_')
    stop_pos = url.find('.html')
    print(url[start_pos+3:stop_pos])

#exercise_4()
def exercise_5():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    #url = input('Enter - ')
    url = 'http://py4e-data.dr-chuck.net/comments_184188.xml'
    html = urllib.request.urlopen(url, context=ctx).read()
    data = html.decode()
    tree = ET.fromstring(data)
    results = tree.findall('.//count')
    sum = 0
    for items in results:
        sum += int(items.text)
    print(sum)
#exercise_5()

def exercise_6():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    #url = input('Enter - ')
    url = 'http://py4e-data.dr-chuck.net/comments_184189.json'
    html = urllib.request.urlopen(url, context=ctx).read()
    data = html.decode()
    info = json.loads(data)
    sum = 0
    for item in info['comments']:
        sum += int(item['count'])
    print(sum)
#exercise_6()

def exercise_7():
    api_key = False
    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    else :
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        address = input('Enter location: ')
        #address = 'University of Ottawa'
        if len(address) < 1: break

        parms = dict()
        parms['address'] = address
        if api_key is not False: parms['key'] = api_key
        url = serviceurl + urllib.parse.urlencode(parms)

        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')

        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            pri nt(data)
            continue
        location = js['results'][0]['place_id']
        print(location)

exercise_7()
