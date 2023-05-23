#!/usr/bin/env python
# coding: utf-8

from random import choice

flights = ["BA","AL","EM","QA","TH","RR"]
fpaths = [789,854,110,215,984,874,115]
cities = ["Oslo","London","Cape Town","Dubai","Seattle","Tokyo","Paris"]

if __name__ == "__main__":
    filename = input("Name the output file? ")
    number_of_items = int(input("How many flights must be generated? "))
    
    with open(f'{filename}.txt','w') as output:
        for i in range(number_of_items):
            flight = choice(flights)
            fpath = choice(fpaths)
            origin = choice(cities)
            dest = choice([c for c in cities if origin != c])
            line = f'{flight}{fpath} : {origin} to {dest}'
            print(line)
            output.write(line+"\n")
    print(f'{__file__} complete! Stopping...')
    input("Press any key to continue...")