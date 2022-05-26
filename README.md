# Collector
Collector is a tool OSINT (open source intelligence) and information gathering. I build this tool for myself but you can use my tool for do OSINT and modify my script.

# Tested On
- Windows
- Kali Linux
- Termux

# Install
**Windows & Kali Linux**
```
git clone https://github.com/galihap76/collector.git
cd collector 
pip install -r requirements.txt
```
**Termux**
```
pkg update && pkg upgrade
pkg install python3
pkg install git
git clone https://github.com/galihap76/collector.git
cd collector
pip install -r requirements.txt
```

# Usage
**Windows**
```
main.py -h
```
**Kali Linux & Termux**
```
python3 main.py -h
```

# Features
- Information gathering in phone numbers
- Information gathering in account github
- Information gathering in ip address
- Information gathering in account instagram

# Example
**Osint Phonenumber**
![Screenshot_2022-05-27_01-29-49 1](https://user-images.githubusercontent.com/83481679/170544327-ddd71936-a5c9-490c-ba4d-c26c8feb277f.png)

# Libraries & Api
- <a href="https://pypi.org/project/requests/">Requests</a>
- <a href="https://api.github.com/">Api github</a>
- <a href="https://pypi.org/project/phonenumbers/">Phone numbers</a>
- <a href="https://ipapi.co/">Ipapi</a>
- <a href="https://github.com/sc1341/InstagramOSINT">Instagram OSINT</a>
