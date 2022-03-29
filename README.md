# Collector
Collector is a tool for osint (open source intelligence) i build this tool for myself and for you if you want use this tool. Collector has been updated but i keep develop this tool to add some features again.

# Install
**Windows & Kali Linux**
```
git clone https://github.com/galihap76/collector.git
cd collector 
pip install -r requirements.txt
```

# Usage
**Windows**
```
main.py -h
```
**Kali Linux**
```
python3 main.py -h
```

# Features
- Information gathering in phone numbers
- Information gathering in account github
- Information gathering in ip address
- Information gathering in account instagram

# Tested On
- Windows
- Kali Linux

# Osint Phonenumber
```
main.py -n +6287848791960
           _ _           _
  ___ ___ | | | ___  ___| |_ ___  _ __
 / __/ _ \| | |/ _ \/ __| __/ _ \| '__|
| (_| (_) | | |  __/ (__| || (_) | |
 \___\___/|_|_|\___|\___|\__\___/|_|


[>] Coded By Galih Ap


[!] Fetching Phone Number : +6287848791960
[+] Country Code: 62 National Number: 87848791960
[+] International Format : +62 878-4879-1960
[+] National Format : 0878-4879-1960
[+] Time Zone : ('Asia/Jakarta',)
[+] ISP : XL
[+] Country Found : Indonesia
[+] Location : Indonesia
```

# Osint Account Github
```
main.py -g Aldi098
           _ _           _
  ___ ___ | | | ___  ___| |_ ___  _ __
 / __/ _ \| | |/ _ \/ __| __/ _ \| '__|
| (_| (_) | | |  __/ (__| || (_) | |
 \___\___/|_|_|\___|\___|\__\___/|_|


[>] Coded By Galih Ap


[!] Fetching On Account Github : Aldi098
[+] login :  Aldi098
[+] id :  89829276
[+] node_id :  MDQ6VXNlcjg5ODI5Mjc2
[+] avatar_url :  https://avatars.githubusercontent.com/u/89829276?v=4
[+] gravatar_id :
[+] url :  https://api.github.com/users/Aldi098
[+] html_url :  https://github.com/Aldi098
[+] followers_url :  https://api.github.com/users/Aldi098/followers
[+] following_url :  https://api.github.com/users/Aldi098/following{/other_user}
[+] gists_url :  https://api.github.com/users/Aldi098/gists{/gist_id}
[+] starred_url :  https://api.github.com/users/Aldi098/starred{/owner}{/repo}
[+] subscriptions_url :  https://api.github.com/users/Aldi098/subscriptions
[+] organizations_url :  https://api.github.com/users/Aldi098/orgs
[+] repos_url :  https://api.github.com/users/Aldi098/repos
[+] events_url :  https://api.github.com/users/Aldi098/events{/privacy}
[+] received_events_url :  https://api.github.com/users/Aldi098/received_events
[+] type :  User
[+] site_admin :  False
[+] name :  XENZI GANZZ
[+] company :  None
[+] blog :
[+] location :  None
[+] email :  None
[+] hireable :  None
[+] bio :  YT : XENZI GANZ 🤖
[+] twitter_username :  None
[+] public_repos :  52
[+] public_gists :  0
[+] followers :  69
[+] following :  2
[+] created_at :  2021-08-31T05:38:02Z
[+] updated_at :  2022-03-12T01:43:43Z
```

# Osint Ip Address
```
main.py -i 103.175.206.70
           _ _           _
  ___ ___ | | | ___  ___| |_ ___  _ __
 / __/ _ \| | |/ _ \/ __| __/ _ \| '__|
| (_| (_) | | |  __/ (__| || (_) | |
 \___\___/|_|_|\___|\___|\__\___/|_|


[>] Coded By Galih Ap


[!] Fetching On Ip : 103.175.206.70
[+] ip :  103.175.206.70
[+] version :  IPv4
[+] city :  Palembang
[+] region :  South Sumatra
[+] region_code :  SS
[+] country :  ID
[+] country_name :  Indonesia
[+] country_code :  ID
[+] country_code_iso3 :  IDN
[+] country_capital :  Jakarta
[+] country_tld :  .id
[+] continent_code :  AS
[+] in_eu :  False
[+] postal :  None
[+] latitude :  -2.9702
[+] longitude :  104.747
[+] timezone :  Asia/Jakarta
[+] utc_offset :  +0700
[+] country_calling_code :  +62
[+] currency :  IDR
[+] currency_name :  Rupiah
[+] languages :  id,en,nl,jv
[+] country_area :  1919440.0
[+] country_population :  267663435
[+] asn :  AS147124
[+] org :  PT Hostingan Awan Indonesia
```

# Osint Account Instagram
```
main.py -ig hacker_zonetamil
           _ _           _
  ___ ___ | | | ___  ___| |_ ___  _ __
 / __/ _ \| | |/ _ \/ __| __/ _ \| '__|
| (_| (_) | | |  __/ (__| || (_) | |
 \___\___/|_|_|\___|\___|\__\___/|_|


[>] Coded By Galih Ap


[!] Current Username: hacker_zonetamil
[+] Username :  hacker_zonetamil
[+] Profile name :  hackerzone
[+] URL :  https://www.instagram.com/hacker_zonetamil/
[+] Followers :  3
[+] Following :  0
[+] Posts :  2
[+] Bio :  ✨ cyber security updates
✨ Ethical hacking
✨ html/java script/coding
✨ dm your queries
✨ education also available
✨ follow us
[+] profile_pic_url :  https://instagram.fsub1-2.fna.fbcdn.net/v/t51.2885-19/258886273_413795847080142_8929442534972858772_n.jpg?stp=dst-jpg_s320x320&_nc_ht=instagram.fsub1-2.fna.fbcdn.net&_nc_cat=106&_nc_ohc=QXtE1wuwiPwAX8qKAsh&edm=ABfd0MgBAAAA&ccb=7-4&oh=00_AT8gzqPbqHVFhFFlEdtaopFKDN9n4efC9xGE8hEEFBp0rg&oe=62478FBE&_nc_sid=7bff83
[+] is_business_account :  True
[+] connected_to_fb :  None
[+] externalurl :  https://youtube.com/channel/UCVDqxrS_705qUwIwfGlclOA
[+] joined_recently :  False
[+] business_category_name :  Creators & Celebrities
[+] is_private :  False
[+] is_verified :  False
[+] Saved data to directory C:\Users\galihap\collector\hacker_zonetamil
[!] If you want do again please remove from saved instagram OSINT!
```
If you do OSINT on instagram automatically you have photo the people and saved on your directory.

**The Result On Profile Picture**

![profile_pic](https://user-images.githubusercontent.com/83481679/160291536-b9cc50de-d5fe-4288-971d-cfc6d3150c19.jpg)

**The Result On Posts**

![FMZXGCHOI](https://user-images.githubusercontent.com/83481679/160291650-e84f00b5-6578-4eba-a014-faa83e73d784.jpg)
![I](https://user-images.githubusercontent.com/83481679/160291684-b1160298-4fe7-4e0d-969b-3ada00dbe2c8.jpg)


# Libraries & Api
- <a href="https://pypi.org/project/requests/">Requests</a>
- <a href="https://pypi.org/project/phonenumbers/">Phone numbers</a>
- <a href="https://ipapi.co/">Ipapi</a>
- <a href="https://github.com/sc1341/InstagramOSINT">Instagram OSINT</a>

# Note
I keep develop this tool if you want use this tool just git clone.
