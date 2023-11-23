#!/usr/bin/env python
import configparser
import psutil
import schedule
import time

from telegram_message import send_message


def check_disk(disk, size):
    free = psutil.disk_usage(disk).free/(1024*1024*1024)
    message: str = f'{free:.4} Gb free on disk {disk}, but needs {size}'
    #print(message)
    if(free > size):
        return
    send_message(message)


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