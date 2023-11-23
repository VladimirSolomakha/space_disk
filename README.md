# Project space_disk
Checking free space on disks and send message it Telegram

### How to run
make clone in ssh
```
git clone git@github.com:VladimirSolomakha/space_disk.git
```
in file 'disks' define paths and time for checking

if needs, install virtual venv
```
apt install python3-venv
```
run activate venv
```
source venv/bin/acivate
```
for install dependencies execute 
```
pip install -r requirements.txt
```
make file '.env' and in this file define 
```
TELEGRAM_TOKEN
TELEGRAM_CHAT_ID
COMPUTER
```
for execute project
```
python3 space_disk.py
```