#! /usr/bin/python3
from math import exp,log,sqrt
import re
import sys
import glob
import os
print('output #145')
inputPath = sys.argv[1]
for input_file in glob.glob(os.path.join(inputPath,'*.py')):
    with open(input_file,'r',newline='') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))
