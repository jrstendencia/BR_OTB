# -*- coding: utf-8 -*-
"""BRA-7.1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17RQ4vG7KNtRbxIlvhQWJqiv8M9qbJeVT

## **Option 2: New Code - Create an IPv4/IPv6 Address Application**

Your manager has received a request from the engineering department for a prototype of a new application that will provide IP addressing information to network technicians.

Search the internet for REST APIs that retrieve a user's current public IPv4 address and IPv6 address, such as ipapi.co or ipsstack.com. Using the public APIs, create a Python application that displays and formats the computer’s current public IP addressing information.

Depending on the API you select, you may also obtain geolocation information, the provider (ISP), the ASN (Autonomous System Number) of the ISP, and country code.

Your manager would also like a list of other enhancements for a future revision. These are called backlog items. This backlog will be used for Project Activity 4.

Note: The objectives and specific tasks of your project will depend on the options provided by the IP information API you choose.

Rubric/Deliverable: The application that your team will work on and the reasons for your choice.
"""

pip install colorama

import requests
from colorama import Fore, Style

def get_ip_info(ip_address=''):
    # Fetch the user's public IP if no specific IP is provided
    if not ip_address:
        response = requests.get('https://ipapi.co/json/').json()
    else:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

    # Check for errors in the response
    if "error" in response:
        return {"Error": response["reason"]}

    ip_info = {
        "IPv4 Address": response.get("ip"),
        "IPv6 Address": response.get("ipv6", "N/A"),  # Handle cases where IPv6 might not be available
        "City": response.get("city", "N/A"),
        "Region": response.get("region", "N/A"),
        "Region Code": response.get("region_code", "N/A"),
        "Country Code": response.get("country", "N/A"),
        "Country Name": response.get("country_name", "N/A"),
        "Country Capital": response.get("country_capital", "N/A"),
        "Continent Code": response.get("continent_code", "N/A"),
        "Latitude": response.get("latitude", "N/A"),
        "Longitude": response.get("longitude", "N/A"),
        "Timezone": response.get("timezone", "N/A"),
        "UTC Offset": response.get("utc_offset", "N/A"),
        "Country Calling Code": response.get("country_calling_code", "N/A"),
        "Currency": response.get("currency", "N/A"),
        "Currency Name": response.get("currency_name", "N/A"),
        "Languages": response.get("languages", "N/A"),
        "ASN": response.get("asn", "N/A"),
        "ISP": response.get("org", "N/A"),
    }

    return ip_info

def print_ip_info(ip_info):
    print("\nThe user's IP addressing information is as follows:")
    print(f"{'Field':<25}{'Value'}")
    print("=" * 55)

    for key, value in ip_info.items():
        if key == "Error":
            print(f"{Fore.RED}{key:<25}{value}{Style.RESET_ALL}")
        else:
            color = Fore.GREEN if key in ["IPv4 Address", "City", "Country Name", "ISP"] else Fore.BLUE
            print(f"{color}{key:<25}{value}{Style.RESET_ALL}")

if __name__ == "__main__":
    ip_address = input("Enter an IP address (leave blank for your public IP): ")
    ip_info = get_ip_info(ip_address)
    print_ip_info(ip_info)

import requests
from colorama import Fore, Style

def get_ip_info(ip_address=''):
    # Fetch the user's public IP if no specific IP is provided
    if not ip_address:
        response = requests.get('https://ipapi.co/json/').json()
    else:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

    # Check for errors in the response
    if "error" in response:
        return {"Error": response["reason"]}

    ip_info = {
        "IPv4 Address": response.get("ip"),
        "IPv6 Address": response.get("ipv6", "N/A"),  # Handle cases where IPv6 might not be available
        "City": response.get("city", "N/A"),
        "Region": response.get("region", "N/A"),
        "Region Code": response.get("region_code", "N/A"),
        "Country Code": response.get("country", "N/A"),
        "Country Name": response.get("country_name", "N/A"),
        "Country Capital": response.get("country_capital", "N/A"),
        "Continent Code": response.get("continent_code", "N/A"),
        "Latitude": response.get("latitude", "N/A"),
        "Longitude": response.get("longitude", "N/A"),
        "Timezone": response.get("timezone", "N/A"),
        "UTC Offset": response.get("utc_offset", "N/A"),
        "Country Calling Code": response.get("country_calling_code", "N/A"),
        "Currency": response.get("currency", "N/A"),
        "Currency Name": response.get("currency_name", "N/A"),
        "Languages": response.get("languages", "N/A"),
        "ASN": response.get("asn", "N/A"),
        "ISP": response.get("org", "N/A"),
    }

    return ip_info

def print_ip_info(ip_info):
    print("\nThe user's IP addressing information is as follows:")
    print(f"{'Field':<25}{'Value'}")
    print("=" * 55)

    for key, value in ip_info.items():
        if key == "Error":
            print(f"{Fore.RED}{key:<25}{value}{Style.RESET_ALL}")
        else:
            color = Fore.GREEN if key in ["IPv4 Address", "City", "Country Name", "ISP"] else Fore.BLUE
            print(f"{color}{key:<25}{value}{Style.RESET_ALL}")

if __name__ == "__main__":
    ip_address = input("Enter an IP address (leave blank for your public IP): ")
    ip_info = get_ip_info(ip_address)
    print_ip_info(ip_info)