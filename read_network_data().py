import csv
import sys

def read_network_data():
    """Reads the network data from the file and returns its name, channel and bssid."""
    file_name = "output-01.csv"
    seperator = ", "
    #The file path needs to be hardcoded.
    path = r"C:\Users\liamb\OneDrive\Desktop\output-01.csv"
    try:
        fp = open(path, 'r')
    except FileNotFoundError: 
            raise FileNotFoundError ("Could not open {}".format(file_name))
    else: 
        with fp as csvfile: 
            network_data = dict()
            for line in fp:
                row = line.strip().split(seperator)
                if row[0] != "" and row[0] != "BSSID" and row[0] != "Station MAC": 
                    network_data [row[0]] = {
                        "first_time_seen": row[1]
                        ,"last_time_seen": row[2] 
                        ,"channel": row[3] 
                        ,"encryption": row[5]
                        #,"name": row[13] It says that the ESSID index is out of range.
                    }
    print("File read!")
    return network_data

read_network_data()




