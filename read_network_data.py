import csv
import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

def read_network_data():
    """Reads the network data from the file and returns its name, channel and bssid."""
    file_name = "output-01.csv"
    seperator = ","
    # The file path needs to be hardcoded.
    path = file_name
    try:
        output_file = open(path, 'r')
    except FileNotFoundError: 
            raise FileNotFoundError ("Could not open {}".format(file_name))
    else: 
        with output_file: 
            network_data = dict()
            table_started = False
            previous_row = ['']
            for line in output_file:
                row = line.strip().replace(" ", "").split(seperator)
                # print(row)
                if row == [''] and previous_row != ['']:
                    break
                elif row[0] == "BSSID":
                    table_started = True
                    continue
                    
                if table_started:                    
                    network_data [row[0]] = {
                        "first_time_seen": row[1],
                        "last_time_seen" : row[2], 
                        "channel"        : row[3],
                        "encryption"     : row[5],
                        "name"           : row[13] 
                    }

                previous_row = row
                
    print("File read!")
    pp.pprint(network_data)

read_network_data()




