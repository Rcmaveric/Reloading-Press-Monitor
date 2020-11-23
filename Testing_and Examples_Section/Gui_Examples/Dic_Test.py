import csv
import pprint
import sys
from collections import namedtuple


def CSV_List():
    data='Recipe'(list)
    with open('data.csv','rb') as data_file:
        reader=csv.DictReader(data_file)
        for row in reader:
            Recipe[row]
            data.append(Recipe)

        print(data)


