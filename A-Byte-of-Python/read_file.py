#!/usr/bin/python3
from math import exp,log,sqrt
import re
from datetime import date,time,datetime,timedelta
import sys
input_file = sys.argv[1]

print ("Output #143:")
filereader = open(input_file,'r')
for row in filereader:
    print (row.strip())
filereader.close()

