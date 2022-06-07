# Collector 🔎 🕵️‍♂️

[![GPLv3](https://img.shields.io/badge/license-GPLv3-blue)](https://img.shields.io/badge/license-GPLv3-blue)
[![Python3](https://img.shields.io/badge/language-Python3-red)](https://img.shields.io/badge/language-Python3-red)

Collector is a OSINT tool and information gathering. I build this tool for myself but you can use my tool for do OSINT.

![carbon (1)](https://user-images.githubusercontent.com/83481679/172416739-1e3b4bbf-ac83-4206-b0d7-8156abaac9aa.png)

# Tested On 
- Windows
- Kali Linux
- Termux

# Install 
```
git clone https://github.com/galihap76/collector.git
cd collector 
pip install -r requirements.txt
```
For termux :
```
pkg update && pkg upgrade
pkg install python3
pkg install git
git clone https://github.com/galihap76/collector.git
cd collector
pip install -r requirements.txt
```

# Usage 
```
python3 main.py -h
```

# Features 
**Information gathering phone numbers**
You can do this on some phone numbers and get isp, country, time zone, country code, national number and international number.

**Information gathering account github**
You can do this on github account and get location, type, followers, following, company, and some data github.

**Information gathering ip address**
You can do this on ip address and get city, version ip, region, latitude, longitude, timezone, and some data ip. You cannot to get accurate ip for this.

**Information gathering account instagram**
You can do this on instagram account and get followers, following, bio, profile picture, save post, and some data instagram. You cannot get information on private profiles.

# Screenshots 📸
![phone-collector 1](https://user-images.githubusercontent.com/83481679/172454033-15d9130b-d609-45fa-b6e4-9f88d742e310.png)
![github-collector 1](https://user-images.githubusercontent.com/83481679/172418954-b9df11e9-9914-4265-b7b5-c3908438ad11.png)
![ipapi-collector 1](https://user-images.githubusercontent.com/83481679/172419647-dcc84c90-5ee9-4c62-ad55-9bb198060f39.png) 
![instagram-collector 1](https://user-images.githubusercontent.com/83481679/172419798-98013374-d6ab-4f46-8e7b-6e4f8803a709.png)
