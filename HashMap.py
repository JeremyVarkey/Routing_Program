class HashMap:

    def __init__(self):
        self.size = 40
        self.map = [None] * self.size

    def getHash(self, key):
        return key % self.size

    def put(self, key, value):
        index = self.getHash(key)
        keyValue = [key, value]

        if self.map[index] is None:
            self.map[index] = list([keyValue])
            return True
        else:
            for pair in self.map[index]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[index].append(keyValue)
            return True

    def get(self, key):
        index = self.getHash(key)

        if self.map[index] is not None:
            for pair in self.map[index]:
                if pair[0] == key:
                    return pair[1]

        return None

    def remove(self, key):
        index = self.getHash(key)

        if self.map[index] is None:
            return False
        else:
            for i in range(0, len(self.map[index])):
                if self.map[index][i][0] == key:
                    self.map[index].pop(i)
                    return True

    def print(self):
        for i in self.map:
            if i is not None:
                print(str(i))



h = HashMap()
h.put(51,'253335')
h.put(67,'45653')
h.put(41,'74564')
h.put(41,'425')
h.print()
h.remove(41)
h.print()
print('Hello, are you looking for package #{}'.format(h.get(67)))
