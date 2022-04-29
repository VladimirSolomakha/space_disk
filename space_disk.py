#!/usr/bin/env python
import configparser
import psutil
import requests
import schedule
import time

HOST = 'http://192.168.1.112:1024/Shops/hs/Tasks/ExchangeTasks'
GUID = 'f7a9a358-f00f-41b0-8618-c42ecd1e8c42'


def check_disk(disk, size):
    free = psutil.disk_usage(disk).free/(1024*1024*1024)
    message: str = f"{free:.4} Gb free on disk {disk}"
    #print(message)
    if(free > size):
        return
    data = {'GUID': GUID,
            'MessageTelegram': message}
    try:
        requests.post(f"{HOST}/", data)
    except:
        print(f'error send post request on disk {disk}')


def main():
    cf = configparser.ConfigParser()
    cf.read('disks')
    count_disks = int(cf.get('options', 'count_disks'))
    for nom in range(1, count_disks+1):
        path = cf.get('disk'+str(nom), 'path')
        size = int(cf.get('disk'+str(nom), 'size'))
        check_disk(path, size)


if __name__ == '__main__':
    """main code"""
    cf = configparser.ConfigParser()
    cf.read('disks')
    count_time = int(cf.get('options', 'count_times'))
    for nom in range(1, count_time+1):
        new_time = cf.get('time', 'time'+str(nom))
        schedule.every().day.at(new_time).do(main)
    while True:
        schedule.run_pending()
        time.sleep(60)
