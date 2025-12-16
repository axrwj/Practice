import time

class DynamicArray:
    def __init__(self, initial_capacity=1):
        self.capacity = initial_capacity
        self.size = 0
        self.data = [None] * self.capacity

    def _resize(self):
        self.capacity *= 2
        new_data = [None] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

    def pushBack(self, value):
        if self.size == self.capacity:
            self._resize()
        self.data[self.size] = value
        self.size += 1

    def __str__(self):
        return str(self.data[:self.size])
class StaticArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0

    def pushBack(self, value):
        if self.size >= self.capacity:
            raise OverflowError("Static array is full")
        self.data[self.size] = value
        self.size += 1
def time_static_array(n=100_000):
    arr = StaticArray(n)
    start = time.perf_counter()
    for i in range(n):
        arr.pushBack(i)
    end = time.perf_counter()
    return end - start

def time_dynamic_array(n=100_000):
    arr = DynamicArray(initial_capacity=1)
    start = time.perf_counter()
    for i in range(n):
        arr.pushBack(i)
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    n = 100_000

    time_static = time_static_array(n)
    time_dynamic = time_dynamic_array(n)

    print(f"Статический массив ({n} элементов): {time_static:.4f} сек")
    print(f"Динамический массив ({n} элементов): {time_dynamic:.4f} сек")
    print(f"Разница: {abs(time_static - time_dynamic):.4f} сек")