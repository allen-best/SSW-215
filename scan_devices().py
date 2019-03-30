import subprocess
import csv
import os
import time

def bash(command, run_time=30, terminate=True):
    """This function runs the input command in the Bash terminal. Modify the run_time variable to manipulate the duration of each scan."""
    if terminate:
        subprocess.call("{}".format(command), shell=True)
    else: 
        try: 
            subprocess.run(command.split(), timeout=run_time)
        except subprocess.TimeoutExpired:
            print("Scan complete!")
    subprocess.call("{}".format(command), shell=True)

def scan_devices():
    """This function scans a single WiFi network and outputs the list of its connected devices as a .csv file to the desktop. 
    To stop scanning the user must enter the keyboard interrupt."""
    bash("echo Conducting Network Scan on '{}'".format(name))
    time.sleep(3)
    try:
        bash('gnome-terminal -x sh -c "airodump-ng --channel {} --bssid {} --write {}_network_output.csv wlan0mon ; bash"'.format(channel, bssid, name))
    except KeyboardInterrupt:
        bash("killall airodump-ng")


"""Populate these variables with the properties of the specific network you want to examine. We will eventually automate this process 
to parse through every network detected by scan_networks(). For that we must consider A)The FOR logic itself and B)Output file naming."""
name = network_name
channel = network_channel
bssid = network_bssid

scan_devices(name, channel, bssid)
