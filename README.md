# Collector 🔎 🕵️‍♂️

![version-1.1.0](https://img.shields.io/badge/version-1.1.0-green)
[![GPLv3](https://img.shields.io/badge/license-GPLv3-blue)](https://img.shields.io/badge/license-GPLv3-blue)
[![Python3](https://img.shields.io/badge/language-Python3-red)](https://img.shields.io/badge/language-Python3-red)

Collector is a OSINT tool and information gathering. I build this tool for my fun and if you like do OSINT maybe you can try this tool.

![carbon (6)](https://user-images.githubusercontent.com/83481679/178091895-24778f4a-5347-4365-aaa1-463fe4d63d50.png)

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
# Login Account Instagram
```
python3 main.py --login -u <YOUR USERNAME> -p <YOUR PASSWORD>
```
# Change Account Instagram
```
python3 main.py --change -u <YOUR USERNAME> -p <YOUR PASSWORD>
```

# Features 
**-Information gathering phone numbers**

You can do this on some phone numbers and get internet service provider, country, time zone, country code, national number and international number.

**-Information gathering github account**

You can do this on github account and get location, type, followers, following, company, and some data github.

**-Information gathering ip address**

You can do this on ip address and get city, version ip, region, latitude, longitude, timezone, and some data ip. You cannot to get accurate ip for this.

**-Information gathering instagram account**

You can do this on instagram account and get followers, following, bio, profile picture, save posts, and some data instagram. You cannot get information on private profiles.

# Screenshots 📸
![phone-collector 1](https://user-images.githubusercontent.com/83481679/172454033-15d9130b-d609-45fa-b6e4-9f88d742e310.png)
![github-collector 1](https://user-images.githubusercontent.com/83481679/172418954-b9df11e9-9914-4265-b7b5-c3908438ad11.png)
![ipapi-collector 1](https://user-images.githubusercontent.com/83481679/172419647-dcc84c90-5ee9-4c62-ad55-9bb198060f39.png) 
![InstagramOSINT-collector 1](https://user-images.githubusercontent.com/83481679/172464501-76efd7b9-878d-40a2-a0bc-8cc3bd982a01.png)
