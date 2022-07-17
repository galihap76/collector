# Collector 🔎 🕵️‍♂️

![version-3.8](https://img.shields.io/badge/version-3.8-green)
[![GPLv3](https://img.shields.io/badge/license-GPLv3-blue)](https://img.shields.io/badge/license-GPLv3-blue)
[![Python3](https://img.shields.io/badge/language-Python3-red)](https://img.shields.io/badge/language-Python3-red)

Collector is a OSINT tool and information gathering. I build this tool for my fun and if you like do OSINT maybe you can try this tool.

![carbon (9)](https://user-images.githubusercontent.com/83481679/179398026-5bfd22db-baa2-45a5-aad8-bade96f04747.png)

# Install 
```
git clone https://github.com/galihap76/collector.git
cd collector 
pip install -r requirements.txt
```

# Options
```
# Help 
python3 main.py -h

# Phone number
python3 main.py -n <phone number>

# Github account
python3 main.py -g <github account>

# Ip address
python3 main.py -i <ip address>

# Instagram account
python3 main.py -ig <instagram account>

# Check update
python3 main.py --update

# Login instagram account
python3 main.py --login -u <YOUR USERNAME> -p <YOUR PASSWORD>

# Change instagram account
python3 main.py --change -u <YOUR USERNAME> -p <YOUR PASSWORD>
```

# Features 
**Information gathering phone numbers**
* Country Code
* National number
* International format
* National format
* Time zone
* ISP
* Location

**Information gathering github account**
* Login
* Id
* Node id
* Avatar url
* Gravatar url
* Url
* Html url
* Followers url
* Following url
* Gists url
* Starred url
* Subscriptions url
* Organizations url
* Repos url
* Events url
* Received events url
* Type
* Site admin
* Name
* Company
* Blog
* Location
* Email
* Hireable
* Bio
* Twitter username
* Public repos
* Public gists
* Followers
* Following
* Created at
* Updated at

**Information gathering ip address**
* Ip
* Version
* City
* Region
* Region code
* Country
* Country name
* Country code
* Country code iso3
* Country capital
* Country tld
* Continent code
* In ue
* Postal
* Latitude
* Longitude
* Timezone
* Utc offset
* Country calling code
* Currency
* Currency name
* Languages
* Country area
* Country population
* Asn
* Org

**Note** 
> You cannot for tracking someone and cannot get accurate public ip.

**Information gathering instagram account**
* Username
* Fullname
* User id
* Number of posts
* Followers
* Following
* Bio
* Is business account
* Business type
* External url
* Is private
* Highlights
* Likes
* Stories
* Download posts & profile picture

**Note**  
> You cannot for do on private account. If you do download highlights or post or maybe stories and profile picture, those will be stored in current directory. Please keep track your request while web scraping instagram. If not you will be given blocking ip, checkpoint account and suspended account.

# Screenshots 📸
![phone-collector 1](https://user-images.githubusercontent.com/83481679/172454033-15d9130b-d609-45fa-b6e4-9f88d742e310.png)
![github-collector 1](https://user-images.githubusercontent.com/83481679/172418954-b9df11e9-9914-4265-b7b5-c3908438ad11.png)
![ipapi-collector 1](https://user-images.githubusercontent.com/83481679/172419647-dcc84c90-5ee9-4c62-ad55-9bb198060f39.png) 
![res](https://user-images.githubusercontent.com/83481679/179392188-77bd6d25-ecbf-4882-8e7f-bd356ac585f0.png)
