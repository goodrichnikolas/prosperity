import pandas as pd
import sys

input_file = sys.argv[1]

def convert_delimiter(file, output_file):
    # Read the file with ';' as the delimiter
    try:
        df = pd.read_csv(file, delimiter=';')
    except:
        df = pd.read_csv(file, delimiter=',')

    # Write the DataFrame back out with ',' as the delimiter
    df.to_csv(output_file, index=False)
    print("File converted successfully")

# Usage
#convert_delimiter('v2.csv', 'v2.csv')
convert_delimiter(input_file, input_file)

