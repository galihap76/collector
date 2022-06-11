#!/usr/bin/env python3
try:
    import argparse, requests, phonenumbers, subprocess
    from instaloader import *
    from phonenumbers import carrier, geocoder, timezone
    
# this when user forget to install some modules
except ModuleNotFoundError:
    import time, sys
    print('[!] Collector need installed some modules')
    time.sleep(2)
    print('[!] Installing modules...')
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
    sys.exit()

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number', type=str, help='do information gathering phone numbers')
parser.add_argument('-g', '--github', type=str, help='do information gathering github account')
parser.add_argument('-i', '--ip', type=str, help='do information gathering ip address')
parser.add_argument('-ig', '--instagram', type=str, help='do information gathering instagram account')
args = parser.parse_args()

class COLLECTOR:
    def __init__(self):
        self.Banner()
        
    # this for banner collector
    def Banner(self):
        print("""
           _ _           _
  ___ ___ | | | ___  ___| |_ ___  _ __
 / __/ _ \| | |/ _ \/ __| __/ _ \| '__|
| (_| (_) | | |  __/ (__| || (_) | |
 \___\___/|_|_|\___|\___|\__\___/|_|
    
    """)
            
    # this is main function
    def Main(self):
        if args.number:
            phone_number = phonenumbers.parse(args.number)
            phone_number_national = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)
            phone_number_international = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            ISP = carrier.name_for_number(phone_number, 'en')
            Time_zone = timezone.time_zones_for_number(phone_number) 
            Country = geocoder.country_name_for_number(phone_number, 'en')
            Location = geocoder.description_for_number(phone_number, 'en') 
            print(f"[!] Fetching Phone Number : {args.number}")
            print(f"[+] {phone_number}")
            print(f"[+] International Format : {phone_number_international}")        
            print(f"[+] National Format : {phone_number_national}")           
            print(f"[+] Time Zone : {Time_zone}")
            print(f"[+] ISP : {ISP}")
            print(f"[+] Country Found : {Country}")
                
        elif args.github:
            username = args.github
            url = f'https://api.github.com/users/{username}'
            response = requests.get(url)
            if response.status_code == 200 and requests.codes.ok:
                data = response.json()
                print( f'[!] Fetching On Github Account : {username}')
                for i in data:
                    print(f'[+] {i} : ',data[i])
                       
        elif args.ip:
            ip = args.ip
            url = f'https://ipapi.co/{ip}/json/'
            response = requests.get(url)
            data = response.json()
            for i in data:
                print(f'[+] {i} : ',data[i])
                
        elif args.instagram:
            print('[!] Waiting...')
            bot = instaloader.Instaloader()
            username = args.instagram
            profile = instaloader.Profile.from_username(bot.context, username)
            posts = profile.get_posts()
            private = profile.is_private
            business = profile.is_business_account
            url = profile.external_url
            business_type = profile.business_category_name
            profile = instaloader.Profile.from_username(bot.context, username)
            print("[+] Username : ", profile.username)
            print("[+] User ID : ", profile.userid)
            print("[+] Number of Posts : ", profile.mediacount)
            print("[+] Followers : ", profile.followers)
            print("[+] Following : ", profile.followees)
            print("[+] Bio : ", profile.biography,profile.external_url)
            print(f'[+] Is business account : {business}')
            print(f'[+] Business type : {business_type}')
            print(f'[+] External url : {url}')
            print(f'[+] Is private : {private}')
            bot.download_profile(username, profile_pic_only = True)
            for index, post in enumerate(posts, 1):
                bot.download_post(post, target=f"{profile.username}_{index}")
                
# run the collector
if __name__ == "__main__":
    try:
        RUN = COLLECTOR()
        RUN.Main()
    # handling error
    except KeyboardInterrupt:
        print('^C')
    except requests.exceptions.ConnectionError:
        print("[-] Error connecting")
    except phonenumbers.phonenumberutil.NumberParseException:
        print("[-] Can't detect")
