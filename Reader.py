import csv
from HashMap import HashMap
from Package import Package

#  Returns double of distances between two locations
def get_distance_between(locations, distances, a, b):
    index_a = locations.index(a)
    index_b = locations.index(b)
    return float(distances[min(index_a, index_b)][max(index_a, index_b)])


def get_locations(file):
    locations = []
    with open(file) as distanceFile:
        reader = csv.reader(distanceFile)
        rows = list(reader)[4:]
        for i in range(1, 28):
            location = rows[i][0].split('\n')
            locations.append(location[1].strip(', '))
    locations[16] = '3575 W Valley Central Station bus Loop'
    return locations


def get_distances(file):
    distances = []
    locations = get_locations('WGUPS Distance Table.csv')

    with open(file) as distancefile:
        reader = csv.reader(distancefile)
        matrix = list(reader)
        matrix = matrix[5:]
        for i in range(2, len(locations) + 2):
            values = []
            for j in range(len(locations)):
                values.append(matrix[j][i])
            distances.append(values)
    return distances


def read_packages(file):
    packages = HashMap()  # Create HashMap object to hold packages we are about to read from the packagefile.csv
    with open(file) as csvfile:  # Read each from the csv limiting it to the first 8 columns
        reader = csv.reader(csvfile)
        rows = list(reader)
        rows = rows[5:]

        for row in rows:  # for each row in the csv file, take the column values and place into package object
            temp = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            packages.put(temp.get_id(), temp)  # place package object into HashMap object
            packages.get(temp.get_id()).print_package()

    return packages
