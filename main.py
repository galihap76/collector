#!/usr/bin/env python3
import argparse, requests, re, lib
from lib.cfonts import render
from lib.colorama import Fore, Style
from lib.InstagramOSINT import *
from lib.phonenumbers import carrier
from lib.phonenumbers import geocoder
from lib.phonenumbers import phonenumber
from lib.phonenumbers import timezone

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number', type=str, help='do information gathering on phone numbers')
parser.add_argument('-g', '--github', type=str, help='do information gathering on account github')
parser.add_argument('-i', '--ip', type=str, help='do information gathering on ip')
parser.add_argument('-ig', '--instagram', type=str, help='do information gathering on instagram')
args = parser.parse_args()

def Banner():
    print(Fore.GREEN + """
           _ _           _
  ___ ___ | | | ___  ___| |_ ___  _ __
 / __/ _ \| | |/ _ \/ __| __/ _ \| '__|
| (_| (_) | | |  __/ (__| || (_) | |
 \___\___/|_|_|\___|\___|\__\___/|_|
    
    """)
    print(Fore.GREEN + "[>] Coded By Galih Ap")
    print("\n")

def Main():
    Banner()
    if args.number:
        try:
            phone_number = lib.phonenumbers.parse(args.number)
            phone_number_national = lib.phonenumbers.format_number(phone_number, lib.phonenumbers.PhoneNumberFormat.NATIONAL)
            phone_number_international = lib.phonenumbers.format_number(phone_number, lib.phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            ISP = carrier.name_for_number(phone_number, 'en')
            Time_zone = timezone.time_zones_for_number(phone_number) 
            Country = geocoder.country_name_for_number(phone_number, 'en')
            Location = geocoder.description_for_number(phone_number, 'en') 
            print(Fore.YELLOW + f"[!] Fetching Phone Number : {args.number}")
            print(Fore.GREEN + f"[+] {phone_number}")
            print(Fore.GREEN + f"[+] International Format : {phone_number_international}")        
            print(Fore.GREEN + f"[+] National Format : {phone_number_national}")           
            print(Fore.GREEN + f"[+] Time Zone : {Time_zone}")
            print(Fore.GREEN + f"[+] ISP : {ISP}")
            print(Fore.GREEN + f"[+] Country Found : {Country}")
            print(Fore.GREEN + f"[+] Location : {Location}")
        except KeyboardInterrupt:
            print(Fore.RED + "[-] Exit")
        except lib.phonenumbers.phonenumberutil.NumberParseException:
            print(Fore.RED + "[-] WRONG COMMAND!")
            print(Fore.YELLOW + "[!] Example you must enterred like this : +62xxxxx")
        except KeyboardInterrupt:
            print(Fore.RED + "[-] Exit")
    
    elif args.github:
        try:
            username = args.github
            url = f'https://api.github.com/users/{username}'
            response = requests.get(url)
            if response.status_code == 200 and requests.codes.ok:
                data = response.json()
                print(Fore.YELLOW + f'[!] Fetching On Account Github : {username}')
                for i in data:
                    print(Fore.GREEN + f'[+] {i} : ',data[i])
        except KeyboardInterrupt:
            print(Fore.RED + '[-] Exit')
        except requests.exceptions.ConnectionError:
            print(Fore.RED + "[-] Error connecting!")
        except ValueError:
            print(Fore.RED + '[-] Ip address not valid!')
            
    elif args.ip:
        try:
            if True:           
                ip = args.ip
                url = f'https://ipapi.co/{ip}/json/'
                response = requests.get(url)
                data = response.json()
                match = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
                for valid in ip.split('.'):
                    if int(valid) < 0 or int(valid) > 255 or int(valid) == 0000:
                        print(Fore.RED + '-------------INFO-------------')
                        break
                        exit
                print(Fore.YELLOW + f'[!] Fetching On Ip : {ip}')
                for i in data:             
                    print(Fore.GREEN + f'[+] {i} : ',data[i])
        except KeyboardInterrupt:
            print(Fore.RED + '[-] Exit')
        except requests.exceptions.ConnectionError:
            print(Fore.RED + "[-] Error connecting")
        except ValueError:
            print(Fore.RED + '[-] Ip address not valid!')
    
    elif args.instagram:
        try:
            user_instagram = InstagramOSINT(username=args.instagram)
            data_ig = user_instagram.profile_data
            print(Fore.YELLOW + f'[!] {user_instagram}')
            for i in data_ig:
                print(Fore.GREEN + f'[+] {i} : ',data_ig[i])
            user_instagram.scrape_posts()
            user_instagram.save_data()
            user_instagram.warning_saved()
        except requests.exceptions.ConnectionError:
            print(Fore.RED + "[-] Error connecting")
        except NameError:
            print(Fore.RED + '[-] Not found!')
        except KeyboardInterrupt:
            user_instagram.save_data()
            print(Fore.RED + '[-] Exit')
            user_instagram.warning_saved()
        except IndexError:
            user_instagram.save_data()
            user_instagram.warning_saved()
            pass
        except FileExistsError:
            print(Fore.RED + '[-] You need to remove directory on output saved from data instagram if you want to do osint instagram again!')

if __name__ == "__main__":
    Main()