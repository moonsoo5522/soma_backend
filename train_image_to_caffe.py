import os
import urllib2
import json
from pandas import Series, DataFrame
import pandas as pd

server_url = "http://192.168.99.100:5000/classify_url?imageurl="

number_list = []
cate_list = []

image_count = 0

def search(dirname):
    filenames = os.listdir(dirname)

    global image_count
    length = len(number_list)
    for filename in filenames:
        if length > image_count:
            image_count+=1
            continue
        if(os.path.getsize('C:/Users/user/workspace/test/WebContent/soma_train/'+filename) == 0):
            number_list.append(int(filename.split('.')[0]))
            cate_list.append('broken_file')
            print 'broken file...T_T'
            image_count+=1
            continue

        if(filename.endswith('.jpg')):
            dict = json.load(http_label_request(filename.decode('utf-8')))

            number_list.append(int(filename.split('.')[0]))
            cate_list.append(dict['result'][1][0][0])
            print dict['result']
            image_count+=1

            print filename, dict['result'][1][0][0], str((float)(float(image_count) / 100.0)) + "%"

            if(image_count % 50 == 0):
                data = {'image': cate_list}
                frame = DataFrame(data, index=number_list)
                pd.to_pickle(frame, 'C:/Users/user/Desktop/image.df')

def http_label_request(image_name):
    return urllib2.urlopen(server_url+"http://192.168.99.1:8080/test/soma_train/"+image_name)

def init_list(train_df):
    global image_count
    for each in train_df.iterrows():
        number_list.append(each[0])
        cate_list.append(each[1]['image'])

#train_df = pd.read_pickle("C:/Users/user/Desktop/image.df")
#init_list(train_df)

search("C:/Users/user/workspace/test/WebContent/soma_train/")

data = {'image': cate_list}
frame = DataFrame(data, index = number_list)
pd.to_pickle(frame, 'C:/Users/user/Desktop/image.df')
#dic = json.load(http_label_request("90985.jpg"))

#print dic['result']

#http://192.168.124.36:8080/test/soma_train/