import requests
from time import sleep
import os

def print_header():
    os.system("clear")  # Clears screen
    print("\033[92m" + "╔══════════════════════════════════════════╗")
    print("║         IP Address Information Tool      ║")
    print("╚══════════════════════════════════════════╝" + "\033[0m")
    print("\033[92m" + "Created by: Maleesh's IP Finder v1.0" + "\033[0m")
    print("\n")

def print_info(title, value):
    print(f"\033[92m{title:12} :\033[0m {value}")

def get_ip_info(ip_address):
    print_header()
    print("\033[92mGathering data...\033[0m")
    sleep(1)  # Small delay for effect
    url = f"http://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print_info("IP Address", data.get("ip", "N/A"))
            print_info("City", data.get("city", "N/A"))
            print_info("Region", data.get("region", "N/A"))
            print_info("Country", data.get("country", "N/A"))
            print_info("Location", data.get("loc", "N/A"))
            print_info("Organization", data.get("org", "N/A"))
            print_info("Postal Code", data.get("postal", "N/A"))
            print_info("Timezone", data.get("timezone", "N/A"))
        else:
            print("\033[91mError fetching data. Check the IP address and try again.\033[0m")
    except requests.RequestException:
        print("\033[91mNetwork error. Check your connection.\033[0m")

if __name__ == "__main__":
    print_header()
    ip_address = input("\033[92mEnter IP address: \033[0m")
    get_ip_info(ip_address)
