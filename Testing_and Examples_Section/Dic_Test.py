import csv
import pprint
import sys
from collections import namedtuple


def CSV_List():
    #open file in read mode
    with open('3_3_Cartridge_Recipe.csv', 'r', newline='') as f:
        recipe_list = []
        #pass the file object to dict reader to get dictionary
        reader = csv.DictReader(f)
        for i in reader:
           recipe_list.append(i)
        return recipe_list

        #print(recipe_list)

recipies = CSV_List()
print(recipies[0]['cartridge'])
