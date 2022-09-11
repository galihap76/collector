# Collector 🔎 🕵️‍♂️

![version-3.8](https://img.shields.io/badge/version-3.8-green)
[![GPLv3](https://img.shields.io/badge/license-GPLv3-blue)](https://img.shields.io/badge/license-GPLv3-blue)
[![Python3](https://img.shields.io/badge/language-Python3-red)](https://img.shields.io/badge/language-Python3-red)

Collector is a OSINT tool and information gathering. I build this tool for my fun and you can use this tool for do OSINT. In github account and instagram account you can find information by username.

![carbon (10)](https://user-images.githubusercontent.com/83481679/179400490-0ae38198-4792-4984-806c-c48b13806479.png)

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
python3 main.py -g <target username>

# Ip address
python3 main.py -i <ip address>

# Instagram account
python3 main.py -ig <target username>

# Check update
python3 main.py --update

# Login instagram account
python3 main.py --login -u <YOUR USERNAME> -p <YOUR PASSWORD>

# Change instagram account
python3 main.py --change -u <YOUR USERNAME> -p <YOUR PASSWORD>
```

# Features 
**Information gathering phone numbers**
* Country code
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
![phone-collector](https://user-images.githubusercontent.com/83481679/179906125-01bf07b1-fb12-479c-bd2e-7727278a67ff.png)
![github-collector 1](https://user-images.githubusercontent.com/83481679/172418954-b9df11e9-9914-4265-b7b5-c3908438ad11.png)
![ipapi-collector 1](https://user-images.githubusercontent.com/83481679/172419647-dcc84c90-5ee9-4c62-ad55-9bb198060f39.png) 
![instagram-collector](https://user-images.githubusercontent.com/83481679/179906132-69d7e8a1-0ffe-4776-82af-e784b263b7f0.png)

# Note 📌
I repeat again this tool for my fun and now at 11/09/2022 i can't do update again this tool. Why? because i already busy now for do my real work and other reason is too much eat time if i do update this tool again. I know my code is not good and need to refactoring code. 

I found bug in my tool when i using my termux and when i git clone this tool on other computers. So, if you want to fix the bug or contribute just pull request and i will accept if your code is suitable. Thank you!
