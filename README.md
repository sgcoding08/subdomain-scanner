# Subdomain Finder

A simple Python tool to find live subdomains of a given domain using DNS resolution and a wordlist.

# Features

- Checks subdomains using DNS resolution (no brute force or HTTP checks)
- Supports custom wordlist
- Automatically filters for only live subdomains
- Saves results
- Lightweight 

# Requirements

- Python 3.x
- Internet connection (for DNS resolution)

No external libraries required — uses  `socket` and `time`

