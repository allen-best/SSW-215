import subprocess
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