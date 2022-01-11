from HashMap import HashMap
from Graph import Graph
from Package import Package
import csv

if __name__ == '__main__':
    packages = HashMap()  # Create HashMap object to hold packages we are about to read from the packagefile.csv
    with open('WGUPS Package File.csv') as csvfile:  # Read each from the csv limiting it to the first 8 columns
        reader = csv.reader(csvfile)
        rows = list(reader)
        rows = rows[8:]

        for row in rows:  # for each row in the csv file, take the column values and place into package object
            temp = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            packages.put(temp.get_id(), temp)  # place package object into HashMap object
            # packages.get(temp.get_id()).print_package()

    with open('WGUPS Distance Table.csv') as distancefile:
        reader = csv.reader(distancefile)
        rows = list(reader)
        rows = rows[4:]

        for row in rows:
            print(row)

        locations = Graph()  # Create undirected graph object

        for row in range(1, 28):
            column = 2
            while float(rows[row][column]) != 0.0:
                locations.add_undirected_edge(rows[row][0], rows[0][column], float(rows[row][column]))
                column += 1

        locations.print_contents()
