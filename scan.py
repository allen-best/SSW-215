#!/usr/bin/env python
import subprocess
import csv
import os
import time

class WiFiScan:
    """Gathers data from local area WiFi networks and their devices."""
    def __init__(self, scanned_networks, scanned_devices, file_name, dirc=os.getcwd()):
        """The init method instantiates the list of scanned networks and devices. It also runs the full automation process."""
        os.chdir(dirc)
        #Format for this dictionary is scanned networks' {BSSID: [name, channel, encryption, time_scanned]}.
        self.scanned_networks = dict() 
        #Format for this dictionary is potential matches' {BSSID: [station, channel, name, time_scanned]}.
        self.scanned_devices = dict() 
        #This function results in an output .csv file of scanned network information.
        self.scan_networks() 
        #This function results in an output .csv file of scanned device information.
        self.scan_devices() 
        self.clean_up(["output-01.csv"])

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




def main():
    WiFiScan()
    

if __name__ == "__main__":
    main()
