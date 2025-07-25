import socket
import time

# introduction
print("Welcome to subdomain finder.")
print("Input any website when prompted and this tool will find any common subdomains that are live.")
print("")

# Get domain
domain_name = input("Enter domain name (e.g. google.com): ")

# Open wordlist and results file
with open('wordlist.txt', 'r') as wordlist, open('results.txt', 'w') as results:
    for line in wordlist:
        sub = line.strip()
        full_domain = f"{sub}.{domain_name}"

        try:
            ip = socket.gethostbyname(full_domain)
            print(f"[+] Found: {full_domain} -> {ip}")
            results.write(f"{full_domain} -> {ip}\n")
        except socket.gaierror:
            pass  # Subdomain does not resolve

        time.sleep(0.5)



