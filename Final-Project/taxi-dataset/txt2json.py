import json
import csv
from tqdm import trange # 方便展示进度条
import time, datetime
import hashlib
import uuid
import random

data_20080202 = []
data_20080203 = []
data_20080204 = []
data_20080205 = []
data_20080206 = []
data_20080207 = []
data_20080208 = []
data_error = []

def create_md5():    #通过MD5的方式创建
    m=hashlib.md5()
    m.update(bytes(str(time.time()) + str(uuid.uuid1()),encoding='utf-8'))
    return m.hexdigest()

# 1 - 10358
for filenum in trange(1, 101):
    csvfile = open('D:\课件\可视化\大作业\\release\\taxi_log_2008_by_id\\' + str(filenum) + '.txt', 'r')
    lines = csvfile.readlines()
    for line in lines:
        temp = {}
        ss = line.split(',') 
        temp['md5'] = create_md5()
        temp['id'] = temp['md5']
        temp['phone'] = ''
        # 转为时间数组
        timeArray = time.strptime(ss[1], "%Y-%m-%d %H:%M:%S")
        # 转化为时间戳
        timeStamp = int(time.mktime(timeArray))*1000
        temp['recitime'] = timeStamp
        temp['lng'] = float(ss[2])  # 经度
        temp['lat'] = float(ss[3])  # 维度
        temp['tag'] = 1
        temp['content'] = ''
        temp['conntime'] = None
        temp['user'] = int(ss[0])

        if temp['lng'] >= 116.07893 and temp['lng'] <= 116.75902 and temp['lat'] >= 39.72266 and temp['lat'] <= 40.11607:
            if ss[1].find('2008-02-02') != -1:
                data_20080202.append(temp)
            elif ss[1].find('2008-02-03') != -1:
                data_20080203.append(temp)
            elif ss[1].find('2008-02-04') != -1:
                data_20080204.append(temp)
            elif ss[1].find('2008-02-05') != -1:
                data_20080205.append(temp)
            elif ss[1].find('2008-02-06') != -1:
                data_20080206.append(temp)
            elif ss[1].find('2008-02-07') != -1:
                data_20080207.append(temp)
            elif ss[1].find('2008-02-08') != -1:
                data_20080208.append(temp)
            else:
                data_error.append(temp)

    csvfile.close()


jsonfile_2 = 'data_20080202.json'
with open(jsonfile_2, 'w') as f_obj:
    json.dump(data_20080202, f_obj)

jsonfile_3 = 'data_20080203.json'
with open(jsonfile_3, 'w') as f_obj:
    json.dump(data_20080203, f_obj)

jsonfile_4 = 'data_20080204.json'
with open(jsonfile_4, 'w') as f_obj:
    json.dump(data_20080204, f_obj)

jsonfile_5 = 'data_20080205.json'
with open(jsonfile_5, 'w') as f_obj:
    json.dump(data_20080205, f_obj)

jsonfile_6 = 'data_20080206.json'
with open(jsonfile_6, 'w') as f_obj:
    json.dump(data_20080206, f_obj)

jsonfile_7 = 'data_20080207.json'
with open(jsonfile_7, 'w') as f_obj:
    json.dump(data_20080207, f_obj)

jsonfile_8 = 'data_20080208.json'
with open(jsonfile_8, 'w') as f_obj:
    json.dump(data_20080208, f_obj)

jsonfile_error = 'data_error.json'
with open(jsonfile_error, 'w') as f_obj:
    json.dump(data_error, f_obj)


