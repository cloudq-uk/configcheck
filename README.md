# config check
Python/NAPALM script to check devices and update missing config if needed.

Devices to be checked will require SSH access enabled, and SCP server enabled:

ip scp server enable

Update the 'device_ip_addresses.txt' file with the devices to be checked

Update the 'ios_msdp_groups.cfg' with the config to be checked on the device and applied if missing
