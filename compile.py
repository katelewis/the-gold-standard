#!/usr/bin/python
import csv
import glob
import os
import sys
import pandas as pd
import numpy as np


## This script compiles all files into one csv file
## python compile.py input_path output_file
## python compile.py C:\Users\KateLynnLewis\Documents\ENT_data all_data.csv

input_path = sys.argv[1]
output_file = open(sys.argv[2], 'w')


filewriter = csv.writer(output_file, delimiter=',')
file_counter = 0
print(input_path)
## Change file type to read different file types
file_type = '*.ENT'
for input_file in glob.glob(os.path.join(input_path,file_type)):
        with open(input_file,'rU') as csv_file:
                filereader = csv.reader(csv_file, delimiter=';')
                print(file_counter)

                header = next(filereader,None)
                for row in filereader:
                        filewriter.writerow(row)

        file_counter += 1


output_file.close()