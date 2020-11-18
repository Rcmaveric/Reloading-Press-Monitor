import csv
#Note to self: the way this works is the csv is turned into a class. The class name is the list ID which is Recipe[n],
#where N is the number of the recipe with 0 being the first line. After that the heading can be use as a dot atribut,
#IE Recipe[0].cartridge will give you the cartridge name of recipe 0.
with open('3_3_Cartridge_Recipe.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames

    class Recipe:
        def __init__(self, **fields):
            self.__dict__.update(**fields)

        def __repr__(self):  # Added to make printing instances show their contents.
            fields = ','.join(('{}={!r}'.format(fieldname, getattr(self, fieldname))
                                   for fieldname in fieldnames))
            return('{}({})'.format(self.__class__.__name__, fields))

    Recipe = [Recipe(**row) for row in reader]

print(Recipe[0])