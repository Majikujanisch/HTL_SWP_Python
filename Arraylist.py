import time
class ArrayList:
    def __init__(self, size=10):
        self.max_size = size # maximum memory capacity
        self.list = [None] * self.max_size # allocate array
        self.size = 0 # current actual size (number of elements)

    def add(self, value):
        if self.size >= self.max_size: # check if enough memory capacity
            self._increase_size()
        self.list[self.size] = value
        self.size += 1

    def _increase_size(self):
        new_max_size = self.max_size * 2 # double memory size
        new_list = [None] * new_max_size
        for i in range(0, self.max_size): # copy old list to new list
            new_list[i] = self.list[i]
        self.max_size = new_max_size
        self.list = new_list

    def get(self, index):
        if index >= self.size or index < 0:
            raise Exception('Invalid index')

        return self.list[index]

    def delete(self, index):
        if index >= self.size or index < 0:
            raise Exception('Invalid index')

        # shift list from deleted index onwards
        # element before index are not affected by deletion
        for i in range(index, self.size):
            self.list[index] = self.list[index+1]

        self.size -= 1
    def set(self, index, value):
        self.list.__setitem__(index, value)
    def ShowArray(self):
        for i in range(self.size):
            print(self.get(i))
    def SortAsc(self):
        for i in range(1, self.size):
            key = self.get(i)
            j = i - 1

            while j >= 0 and key < self.get(j):
                self.set(j+1,self.get(j))
                j -= 1
            self.set(j + 1, key)

    def SortDesc(self):
        for i in range(1, self.size):
            key = self.get(i)
            j = i - 1

            while j >= 0 and key > self.get(j):
                self.set(j+1,self.get(j))
                j -= 1
            self.set(j + 1, key)

    def FillTime(self, it):
        timebefore = time.time()
        for i in range(len(it)):
            self.add(it[i])
        timeafter = time.time()
        return timeafter-timebefore

    def SortAscTest(self):
        index = 0
        for i in range(1, self.size):
            key = self.get(i)
            j = i - 1

            while j >= 0 and key < self.get(j):
                self.set(j+1,self.get(j))
                j -= 1
                index+=1
            self.set(j + 1, key)
        return index
    def SortTimeAsc(self):
        before = time.time()
        index = self.SortAscTest()
        after = time.time()
        return index, after-before