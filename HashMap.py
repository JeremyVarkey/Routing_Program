class HashMap:
    #  Constructor, create initial Hashamp with size of 40, unless otherwise specified
    #  Space time complexity: O(1)
    def __init__(self, size=40):
        self.size = size
        self.map = [None] * self.size

    #  Very simple hash function using mod of input
    #  Space time complexity: O(1)
    def get_hash(self, key):
        return key % self.size

    #  Put key(package ID) and value(package) into map from constructor
    #  Space time complexity: O(N)
    def put(self, key, value):
        index = self.get_hash(int(key))  # find index to place key and value pair in HashMap
        keyValue = [key, value]  # make key value pair list

        if self.map[index] is None:  # if index is empty, then place key value pair into index
            self.map[index] = list([keyValue])
            return True
        else:
            for pair in self.map[index]:  # if index is not empty, check to see if key is existing and replace value if so
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[index].append(keyValue)  # if index is not empty, and no identical key is found, append to list at index
            return True

    #  Get package based on inputted key, looking through chaining if needed
    #  Space time complexity: O(N)
    def get(self, key):
        index = self.get_hash(int(key))

        if self.map[index] is not None:
            for pair in self.map[index]:
                if int(pair[0]) == int(key):
                    return pair[1]

        return None

    #  Remove a package from hashmap based on specified key
    #  Space time complexity: O(N)
    def remove(self, key):
        index = self.get_hash(key)

        if self.map[index] is None:
            return False
        else:
            for i in range(0, len(self.map[index])):
                if self.map[index][i][0] == key:
                    self.map[index].pop(i)
                    return True

    #  Return hashmap
    #  Space time complexity: O(1)
    def get_map(self):
        return self.map

    #  Print contents of hashmap
    #  Space time complexity: O(1)
    def print(self):
        for i in self.map:
            if i is not None:
                print(i)


