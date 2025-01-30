import socket
import requests
import json

def find_subdomains(domain):
    """Find subdomains of a given domain and resolve their IP addresses."""
    try:
        # Use a subdomain enumeration API like crt.sh
        url = f"https://crt.sh/?q={domain}&output=json"
        response = requests.get(url)
        
        if response.status_code != 200:
            print("Failed to fetch data from crt.sh")
            return []

        data = response.json()
        subdomains = set()

        for entry in data:
            name = entry.get("name_value", "")
            subdomains.update(name.split("\n"))

        subdomains = list(subdomains)

        # Resolve IP addresses
        subdomain_ips = {}
        for sub in subdomains:
            try:
                ip = socket.gethostbyname(sub)
                subdomain_ips[sub] = ip
            except socket.gaierror:
                subdomain_ips[sub] = "Could not resolve"

        return subdomain_ips

    except Exception as e:
        print(f"Error: {e}")
        return {}

# Example Usage
domain = "example.com"
results = find_subdomains(domain)

for sub, ip in results.items():
    print(f"{sub} -> {ip}")