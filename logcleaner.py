#Load the most recent log file and clean it up

import pandas as pd
import re
import os

#Get the most recent file that ends with .log in the cwd
def get_recent_log_file():
    files = os.listdir()
    log_files = [f for f in files if f.endswith('.log')]
    log_files.sort(key=os.path.getmtime, reverse=True)
    return log_files[0]

most_recent_log = get_recent_log_file()

#Load the log file into a string
with open(most_recent_log, 'r') as file:
    log = file.read()

print(log)