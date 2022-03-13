class HashMap:
    # Construct
    def __init__(self, size=40):
        self.size = size
        self.map = [None] * self.size

    # very simple hash function
    def get_hash(self, key):
        return key % self.size

    # put key(package ID) and value(package) into map from constructor
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

    # get package based on inputted key
    def get(self, key):
        index = self.get_hash(int(key))

        if self.map[index] is not None:
            for pair in self.map[index]:
                if pair[0] == key:
                    return pair[1]

        return None

    def remove(self, key):
        index = self.get_hash(key)

        if self.map[index] is None:
            return False
        else:
            for i in range(0, len(self.map[index])):
                if self.map[index][i][0] == key:
                    self.map[index].pop(i)
                    return True

    def get_map(self):
        return self.map

    def print(self):
        for i in self.map:
            if i is not None:
                print(i)


