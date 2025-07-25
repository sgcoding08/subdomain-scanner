#imports
import socket
import time

#input value and program introduction
print(" ")
print("welcome to subdomain finder. input any website when promted and this tool will find any and all common subdomains belonging to that website")
print(" ")
domain_name = input("enter domain name (eg: google.com): ")

#open subdomain list and results
wordlist = open('wordlist.txt')
results = open('results.txt', 'w')

#join domain and all subdomains
for line in wordlist: 
    sub = line.strip()
    full_domain = f"{sub}.{domain_name}"

    #resolve domain to an ip
    try:
        ip = socket.gethostbyname(full_domain)  
        print(f"[+] Found: {full_domain} -> {ip}")
        results.write(f"{full_domain} -> {ip}\n")


    except socket.gaierror:
        pass  

    time.sleep(0.5)




