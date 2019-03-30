import subprocess
import csv
import os
import time

def bash(command):
    """This function runs the input command in the Bash terminal."""
    subprocess.call("{}".format(command), shell=True)

def scan_networks():
    """This method scans for WiFi networks and outputs them as a .csv file to the desktop. To stop scanning the user must enter the keyboard interrupt."""
    bash("echo Enabling Monitor Mode")
    time.sleep(3)
    bash("airmon-ng start wlan0")
    bash("echo Conducting Network Scan")
    time.sleep(3)
    bash("airodump-ng start wlan0mon")
    try:
        bash("airodump-ng wlan0mon -w output --output-format csv")
    except KeyboardInterrupt:
        bash("killall airodump-ng")

scan_networks()

