#!/usr/bin/python3
with open('pi.txt') as file_object:
    #contents = file_object.read()
    #print(contents.rstrip())
    for line in file_object:
        print(line)
