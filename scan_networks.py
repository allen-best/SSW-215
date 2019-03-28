import subprocess
import csv
import os
import time

def bash(self, command):
        """This function runs the input command in the Bash terminal."""
        subprocess.call("{}".format(command), shell=True)

def scan_networks(self):
    """This method scans for WiFi networks and outputs them as a .csv file to the desktop. To stop scanning the user must enter the keyboard interrupt."""
    self.bash("echo Resetting Device")
    time.sleep(1)
    self.bash("airmon-ng check kill")
    self.bash("echo Enabling Monitor Mode")
    time.sleep(1)
    self.bash("airmon-ng start wlan0")
    self.bash("echo Conducting Network Scan")
    time.sleep(1)
    self.bash("airodump-ng start wlan0mon")
    try:
        self.bash("airodump-ng wlan0 -w output --output-format csv")
    except KeyboardInterrupt:
        self.bash("killall airodump-ng")

scan_networks()