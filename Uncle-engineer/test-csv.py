# test-csv.py

import csv


def writetocsv(data):
    with open('data.csv', 'a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)

data = ['Mango', 20]
writetocsv(data)
