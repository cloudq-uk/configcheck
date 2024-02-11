import json
from napalm import get_network_driver
from getpass import getpass

def process_device(ip, username, password):
    try:
        driver = get_network_driver('ios')
        ios_device = driver(ip, username, password)
        ios_device.open()

        print(f'Checking {ip}')
        ios_device.load_merge_candidate(filename='ios_msdp_groups.cfg')

        diffs = ios_device.compare_config()
        if len(diffs) > 0:
            print(diffs)
            ios_device.commit_config()
        else:
            print('No changes required.')
            ios_device.discard_config()

        ios_device.close()

    except Exception as e:
        print(f"Error: Unable to process {ip}. {str(e)}")

if __name__ == "__main__":
    # Username and Password prompt
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    # Define the path to the file containing IP addresses
    device_list = "device_ip_addresses.txt"

    try:
        with open(device_list, 'r') as file:
            # Read IP addresses from the file
            ip_addresses = file.readlines()

            # Loop through each IP address and process the device
            for ip in ip_addresses:
                ip = ip.strip()  # Remove leading/trailing whitespaces
                process_device(ip, username, password)

    except FileNotFoundError:
        print(f"Error: The file '{device_list}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")
