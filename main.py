#!/usr/bin/env python3
try:
    import argparse, requests, phonenumbers, time, sys, os, webbrowser
    from os import name
    from prettytable import PrettyTable
    from instaloader import *
    from phonenumbers import carrier, geocoder, timezone
    
# this when user forget to install some modules
except ModuleNotFoundError:
    import time, sys, subprocess
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
parser.add_argument('-l', '--login', type=str, help='login your account instagram[REQUIRED]')
args = parser.parse_args()

class Collector:
    def __init__(self):
        self.Banner()
        self.L = instaloader.Instaloader()

    # this for banner collector
    def Banner(self):
        print("""
           _ _           _
  ___ ___ | | | ___  ___| |_ ___  _ __
 / __/ _ \| | |/ _ \/ __| __/ _ \| '__|
| (_| (_) | | |  __/ (__| || (_) | |
 \___\___/|_|_|\___|\___|\__\___/|_|
    
    """)
           
    def Asking_else(self):
        print("[-] Collector can't understand what do you mean")
        time.sleep(2)
        print("[-] Collector has been stopped")
        sys.exit()

    # this is main function
    def Main(self):
        if args.number:
            phone_number = phonenumbers.parse(args.number)
            phone_number_national = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)
            phone_number_international = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            isp = carrier.name_for_number(phone_number, 'en')
            time_zone = timezone.time_zones_for_number(phone_number)
            location = geocoder.description_for_number(phone_number, 'en')

            print(f"[!] Fetching Phone Number : {args.number}")
            print(f"[+] {phone_number}")
            print(f"[+] International Format : {phone_number_international}")        
            print(f"[+] National Format : {phone_number_national}")           
            print(f"[+] Time Zone : {time_zone}")
            print(f"[+] ISP : {isp}")
            print(f"[+] Location : {location}")
                
        elif args.github:
            username = args.github
            url = f'https://api.github.com/users/{username}'
            response = requests.get(url)
            if response.status_code == 200 and requests.codes.ok:
                data = response.json()
                print( f'[!] Fetching on github account : {username}')
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
            print('[+] Waiting...')
            username_read = open('username.txt', 'r')
            password_read = open('password.txt', 'r')
            username = args.instagram
            
            self.L.login(username_read.read(), password_read.read(), proxies=proxies)
            profile = instaloader.Profile.from_username(self.L.context, username)
            private = profile.is_private  
            posts = profile.get_posts()
            full_name = profile.full_name
            business = profile.is_business_account
            url = profile.external_url
            business_type = profile.business_category_name
             
            # check if private account
            if private == True:
                print("[!] Warning private account")
                time.sleep(2)
                print("[-] Collector can't download some posts")
                time.sleep(2)

            print(f"[+] Username : {profile.username}")
            print(f'[+] Fullname : {full_name}')
            print(f"[+] User ID : {profile.userid}")
            print(f"[+] Number of posts : {profile.mediacount}")
            print(f"[+] Followers : {profile.followers}")

            # ask if user want to see some follower accounts but this if not private account
            if private == False:
                ask_followers = input('[!] Do you want to see some follower accounts?[y/n]: ')
                if ask_followers.lower() == 'y':
                    print('[+] Waiting...')
                    Table_follower_accounts = PrettyTable(["FOLLOWER ACCOUNTS"])
                    for follower in profile.get_followers():
                        Table_follower_accounts.add_row([follower])
                    print(Table_follower_accounts)        
                elif ask_followers.lower() == 'n':
                    pass    
                else:
                    self.Asking_else()

            print(f"[+] Following : {profile.followees}")  

            # ask if user want to see some following accounts but this if not private account
            if private == False:     
                ask_followings = input('[!] Do you want to see some following accounts?[y/n]: ')
                if ask_followings.lower() == 'y':
                    print('[+] Waiting...')
                    Table_following_accounts = PrettyTable(["FOLLOWING ACCOUNTS"])
                    for following in profile.get_followees():
                        Table_following_accounts.add_row([following])
                    print(Table_following_accounts)
                elif ask_followings.lower() == 'n':
                    pass
                else:
                    self.Asking_else()

                ask_like_post = input('[!] Do you want to get likes of a post?[y/n]: ')

                if ask_like_post.lower() == 'y':
                    print(f'[!] You need to visit on username {username} and select one of the posts')
                    time.sleep(2)
                    url_instagram = f'https://www.instagram.com/{username}'
                    for item in list(os.environ.keys()): 
                        if "ANDROID" in item.upper():
                            os.system("termux-open-url \""+url_instagram+"\"") 
                    
                    if name == "nt" or name == "posix":
                        webbrowser.open(url_instagram, new=1, autoraise=True)

                    while True:
                        url_post = input('[!] Please copy the shortlink [https://www.instagram.com/p/(JUST COPY THE SHORTLINK)]: ')

                        if url_post == '':
                            self.Asking_else()           
                        else:
                            print('[+] Waiting...')
                            P = instaloader.Post.from_shortcode(self.L.context, url_post)
                            Table = PrettyTable(["PEOPLE WHO LIKED THE POST"])
                            for like in P.get_likes():
                                Table.add_row([like.username])
                            print(Table)
                        ask_again = input('[!] Do you want do again?[y/n] : ')

                        if ask_again.lower() == 'y':
                            continue
                        elif ask_again.lower() == 'n':
                            break
                        
                elif ask_like_post.lower() == 'n':
                    pass
                else:
                    self.Asking_else()

            print(f"[+] Bio : {profile.biography}")
            print(f'[+] Is business account : {business}')
            print(f'[+] Business type : {business_type}')
            print(f'[+] External url : {url}')
            print(f'[+] Is private : {private}')
        
            if private == False:
                downloads = input('[!] Do you want to download all posts and profile picture?[y/n]: ')
                if downloads.lower() == 'y':
                    print('[+] Ready to download all posts and profile picture...')
                    self.L.download_profile(username, profile_pic_only = True)
                    for index, post in enumerate(posts, 1):
                        self.L.download_post(post, target=f"{profile.username}_{index}")
                    print('[+] Results has been stored in : ',os.getcwd())
                    print('[+] Successfully for scraping')
                elif downloads.lower() == 'n':
                    print('[+] Successfully for scraping')
                else:
                    self.Asking_else()
                
        elif args.login:
            print("""
[1] Add your username and password 
[2] Change your username and password
            """)
            choose = input('[+] Collector : ')
            
            if choose == '1':
                # this for create your username and password
                YOUR_USERNAME = input('[+] Enter your username : ')
                YOUR_PASSWORD = input('[+] Enter your password : ')
                
                username_create = open("username.txt", "a")
                username_create.write(f"{YOUR_USERNAME}")
                username_create.close()
                
                password_create = open("password.txt", "a")
                password_create.write(f"{YOUR_PASSWORD}")
                password_create.close()
                print('[+] Your username and password has been stored in : ',os.getcwd())
                
            elif choose == '2':
                # this for change your username and password
                YOUR_USERNAME = input('[+] Change your username : ')
                YOUR_PASSWORD = input('[+] Change your password : ')
                
                username_change = open('username.txt', 'w')
                username_change.write(f'{YOUR_USERNAME}')
                username_change.close()
                
                password_change = open('password.txt', 'w')
                password_change.write(f'{YOUR_PASSWORD}')
                password_change.close()
                print('[+] Success to change')
                time.sleep(2)
                print('[+] Your username and password has been stored in : ',os.getcwd())

            else:
                self.Asking_else()
                                        
# run the collector
if __name__ == "__main__":
    try:
        RUN = Collector()
        RUN.Main()
    # handling error
    except KeyboardInterrupt:
        print('^C')
    except requests.exceptions.ConnectionError:
        print("[-] Error connecting")
    except phonenumbers.phonenumberutil.NumberParseException:
        print("[-] Can't detect")
        print('[!] Example : +62xxx')
    except InvalidArgumentException:
        import subprocess, time
        from os import system, name
        print("[!] Collector can't login please login now")
        time.sleep(2)
        # this mean for clear screen on windows
        if name == "nt":
            system('cls')

        # this mean for clear screen on mac and linux
        elif name == 'posix':
            system('clear')
        subprocess.run([sys.executable, 'main.py', '-l', 'instagram'])
    except LoginRequiredException:
        import subprocess, sys
        print("[-] Login required")  
        subprocess.run([sys.executable, 'main.py', '-h'])
