class Array:

    def __init__(self, arr):
        self.arr = arr
        self.accesses = 0

    def __getitem__(self, key):
        self.accesses = self.accesses + 1
        return self.arr[key]

    def __str__(self):
        return self.arr.__str__() + (" accesses: " + str(self.accesses))

    def __len__(self):
        return len(self.arr)

    def __setitem__(self, key, value):
        # TODO: count setitem to accesses or not
        self.arr.__setitem__(key, value)

    def swap(self, i, j):
        if i != j:
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
