# -*- coding: utf-8 -*-

import os
import urllib2
import json
from pandas import Series, DataFrame
import pandas as pd

server_url = "http://192.168.99.100:5000/classify_url?imageurl="

url_list = []
cate_list = []
cate_list2 = []
image_count = 0

def search():

    global image_count
    length = len(cate_list) # url_list => cate_list로 변환

    for filename in url_list:
        if length > image_count:
            image_count+=1
            continue
        if(filename == ''):
            image_count+=1
            cate_list.append('broken')
            cate_list2.append('broken')
            continue

        dict = json.load(http_label_request(filename.decode('utf-8')))

        print dict['result']
        if(dict['result'][0] == False):
            image_count+=1
            cate_list.append('broken')
            cate_list2.append('broken')
            continue
        cate_list.append(dict['result'][1][0][0])
        cate_list2.append(dict['result'][2][0][0])

        image_count+=1

        print filename, str((float)(float(image_count) / 49)) + "%"

        if(image_count % 30 == 0):
            data = {'image': cate_list,
                    'image2': cate_list2,
                    'url': url_list[0:image_count]}
            frame = DataFrame(data)
            pd.to_pickle(frame, 'C:/Users/user/Desktop/url-image.df')

def http_label_request(image_name):
    return urllib2.urlopen(server_url+image_name)

def init_list(arg_df):
    global image_count
    for each in arg_df.iterrows():
        cate_list.append(each[1]['image'])
        cate_list2.append(each[1]['image2'])

train_df = pd.read_pickle("C:/Users/user/Desktop/url.df")
reserved_df = pd.read_pickle("C:/Users/user/Desktop/url-image.df")
url_list = train_df.url

init_list(reserved_df)

search()

data = {'image': cate_list,
        'image2': cate_list2,
        'url': url_list}
frame = DataFrame(data)
pd.to_pickle(frame, 'C:/Users/user/Desktop/url-image.df')