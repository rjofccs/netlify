#!/usr/bin/python3
# -*- coding: utf-8 -*-
# pip install arrow requests lxml 
import sys, arrow, os, re, json, requests, threading, urllib3
# from lxml import etree
from urllib.parse import urlparse

now = arrow.utcnow().to('Asia/Shanghai').format('YYYY-MM-DD_HH:mm:ss')
dire = os.path.dirname(os.path.abspath(__file__))
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
output_folder = os.path.abspath(os.path.join(dire, 'tmp')) + '/'

def getdata(url):
    resp = requests.get().content
    return json.load(resp)['data']


def bp():
    respds = getdata("https://api.bilibili.com/x/v3/fav/resource/ids?media_id=59128019&platform=web")
    vid = {}
    for item in respds:
        vid[item['bvid']] = ':'.format(item['id'],item['type'])

    respds = getdata("https://api.bilibili.com/x/v3/fav/resource/infos?resources=".format(','.join(vid.values())))
    tv = {}
    for item in respds:
        tv[item['bvid']] = item['title']

    fw = open(output_folder + 'tmp.txt', 'w')
    for k,v in tv.items():
        fw.writelines(','.join(vid.values()))
    # os.system(''.format(txt1, mp4))

if __name__ == "__main__":
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    bp()