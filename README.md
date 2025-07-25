# 🔍 Subdomain Finder

A simple Python tool to find live subdomains of a given domain using DNS resolution and a wordlist.

## 🚀 Features

- Checks subdomains using DNS resolution (no brute force or HTTP checks)
- Custom wordlist support
- Automatically filters for only live/resolving subdomains
- Saves results to `results.txt`
- Lightweight and easy to extend

## 🛠 Requirements

- Python 3.x
- Internet connection (for DNS resolution)

No external libraries required — uses Python's built-in `socket` and `time`.

## 📦 Usage

```bash
python subfinder.py
