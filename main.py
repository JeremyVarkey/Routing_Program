import HashMap
import csv


with open('WGUPS Package File.csv') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)
    rows = rows[8:]

    for row in rows:
        row = row[:8]
        print(row)


#need to create package object that uses **kwargs to place all items in the list as respective values in the object
#need to add getters and setters for the package object



