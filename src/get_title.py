from urllib3.exceptions import InsecureRequestWarning
from datetime import datetime
from time import sleep
import urllib3
import json
import config

urllib3.disable_warnings(InsecureRequestWarning)

API_URL = 'https://api.syosetu.com/novelapi/api'

FILE_NAME = config.FILE_NAME
LOG_NAME = config.LOG_NAME
SLEEP_TIME = config.SLEEP_TIME
START_ID = config.START_ID
END_ID = config.END_ID

def title_to_list(dicData):
    titles = []
    for i in range(1,len(dicData)):
        titles.append(list(dicData[i].values())[0])
    return titles

def get_title(userid):
    http = urllib3.PoolManager()
    r = http.request('GET',API_URL,fields={'out':'json','of':'t','userid':userid})
    dicData = json.loads(r.data)
    return title_to_list(dicData)

def write_title(titles):
    fout = open(FILE_NAME,'a')
    print(*titles, sep='\n',file = fout)
    fout.close()

def write_log(logText):
    fout = open(LOG_NAME,'a')
    print(logText, sep='\n',file = fout)
    fout.close()


for userID in range(START_ID,END_ID + 1):
    titles = get_title(userID)
    titles = list(filter(lambda str:str != '', titles))
    if len(titles) != 0:
        write_title(titles)
    nowTime = datetime.now()
    logText = 'Time:[{}] ID:{} Count:{}'.format(nowTime,userID,len(titles))
    print(logText)
    write_log(logText)
    sleep(SLEEP_TIME)
