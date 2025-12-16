class StaticArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0

    def _check_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

    def _check_capacity(self):
        if self.size >= self.capacity:
            raise OverflowError("Array is full")

    def pushBack(self, value):
        """
        Сложность: O(1)
        """
        self._check_capacity()
        self.data[self.size] = value
        self.size += 1

    def pushFront(self, value):
        """
        Сложность: O(n)
        """
        self._check_capacity()
        for i in range(self.size, 0, -1):
            self.data[i] = self.data[i - 1]
        self.data[0] = value
        self.size += 1

    def insert(self, index, value):
        """
        Сложность: O(n)
        """
        if index < 0 or index > self.size:
            raise IndexError("Insert index out of range")
        self._check_capacity()
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.size += 1

    def remove(self, index):
        """
        Сложность: O(n)
        """
        self._check_index(index)
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size -= 1

    def find(self, value):
        """
        Сложность: O(n)
        """
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1

    def __str__(self):
        return str(self.data[:self.size])
arr = StaticArray(5)
arr.pushBack(10)
arr.pushBack(20)
arr.pushFront(5)
print(arr)  # [5, 10, 20]

arr.insert(1, 7)
print(arr)  # [5, 7, 10, 20]

arr.remove(2)
print(arr)  # [5, 7, 20]

print(arr.find(7))  # 1
print(arr.find(99))  # -1