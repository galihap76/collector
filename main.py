import phonenumbers, argparse
from phonenumbers import timezone, geocoder, carrier
from cfonts import render
from termcolor import colored
from pyfiglet import Figlet

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number', type=str, help='do information gathering in phone numbers')
args = parser.parse_args()

def Banner():
    f = Figlet(font='standard')
    print(colored(f.renderText('collector'), 'green'))
    print(colored("[>] Coded By Galih Ap", 'green'))
    print("\n")

Banner()

def Main():
    if args.number:
        try: 
            phone_number = phonenumbers.parse(args.number)
            phone_number_national = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)
            phone_number_international = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            ISP = carrier.name_for_number(phone_number, 'en')
            Time_zone = timezone.time_zones_for_number(phone_number) 
            Country = geocoder.country_name_for_number(phone_number, 'en')
            Location = geocoder.description_for_number(phone_number, 'en') 
            print(colored(f"[!] Fetching Phone Number : {args.number}", 'yellow'))
            print(colored(f"[+] {phone_number}", 'green'))
            print(colored(f"[+] International Format : {phone_number_international}", 'green'))           
            print(colored(f"[+] National Format : {phone_number_national}", 'green'))           
            print(colored(f"[+] Time Zone : {Time_zone}", 'green'))
            print(colored(f"[+] ISP : {ISP}", 'green'))
            print(colored(f"[+] Country Found : {Country}", 'green'))
            print(colored(f"[+] Location : {Location}", 'green'))
        except phonenumbers.phonenumberutil.NumberParseException:
            print(colored("[-] WRONG COMMAND!", 'red'))
            print(colored("[!] Example You Must Enterred : +62xxxxx", 'yellow'))
            
if __name__ == "__main__":
    Main()