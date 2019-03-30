import subprocess
import csv
import os
import time
import sys

# def bash(command):
#     """This function runs the input command in the Bash terminal."""
#     subprocess.call("{}".format(command), shell=True)

# def scan_networks():
#     """This method scans for WiFi networks and outputs them as a .csv file to the desktop. To stop scanning the user must enter the keyboard interrupt."""
#     bash("echo Enabling Monitor Mode")
#     time.sleep(3)
#     bash("airmon-ng start wlan0")
#     bash("echo Conducting Network Scan")
#     time.sleep(3)
#     bash("airodump-ng start wlan0mon")
#     try:
#         bash("airodump-ng wlan0mon -w network_scan_output --output-format csv")
#     except KeyboardInterrupt:
#         bash("killall airodump-ng")

# def scan_devices(name, channel, bssid):
#     """This method scans a single WiFi network and outputs the list of its connected devices as a .csv file to the desktop. 
#     To stop scanning the user must enter the keyboard interrupt."""
#     bash("echo Conducting Network Scan on '{}'".format(name))
#     time.sleep(3)
#     try:
#         bash('gnome-terminal -x sh -c "airodump-ng --channel {} --bssid {} --write {}_device_list.csv wlan0mon ; bash"'.format(channel, bssid, name))
#     except KeyboardInterrupt:
#         bash("killall airodump-ng")

def read_files(file_name):
    """Reads the network data from the file and returns its name, channel and bssid."""
    seperator = ", "
    try:
        fp = open(file_name, 'rb')
    except FileNotFoundError:
        raise FileNotFoundError ("Could not open {}".format(file_name))
    else: 
        with fp: 
            scan_data = dict()
            for line in fp:
                row = line.strip.split(seperator)
                if row[0] != "" and row[0] != "BSSID" and row[0] != "Station MAC": 
                    scan_data [row[0]] = {
                        "first_time_seen": row[1],
                        "last_time_seen": row[2], 
                        "channel": row[3], 
                        "encryption": row[5], 
                        "name": row[13]
                    }
            print(scan_data)
                                        


# """Populate these variables with the properties of the specific network you want to examine. We will eventually automate this process 
# to parse through every network detected by scan_networks(). For that we must consider A)The FOR logic itself and B)Output file naming."""
# name = network_name
# channel = network_channel
# bssid = network_bssid

read_files("output-01.csv")
