from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.keyMap = {}                 # key -> [value, freq]
        self.freqMap = defaultdict(OrderedDict)
        self.minFreq = 0

    def get(self, key):
        if key not in self.keyMap:
            return -1

        value, freq = self.keyMap[key]

        # remove from old frequency
        del self.freqMap[freq][key]

        # if that bucket becomes empty
        if not self.freqMap[freq]:
            del self.freqMap[freq]

            if self.minFreq == freq:
                self.minFreq += 1

        # increase frequency
        freq += 1
        self.keyMap[key] = [value, freq]
        self.freqMap[freq][key] = None

        return value

    def put(self, key, value):
        if self.capacity == 0:
            return

        # key already exists
        if key in self.keyMap:
            self.keyMap[key][0] = value
            self.get(key)       # increases frequency
            return

        # cache full
        if len(self.keyMap) == self.capacity:
            # remove LRU key from minimum frequency
            removeKey, _ = self.freqMap[self.minFreq].popitem(last=False)

            del self.keyMap[removeKey]

        # insert new key with freq = 1
        self.keyMap[key] = [value, 1]
        self.freqMap[1][key] = None

        self.minFreq = 1