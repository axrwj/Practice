class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self._data = [None] * capacity
        self._front = 0
        self._size = 0

    def enqueue(self, item):
        """Добавить элемент в конец очереди."""
        if self._size == self.capacity:
            raise OverflowError("Queue is full")

        rear_index = (self._front + self._size) % self.capacity
        self._data[rear_index] = item
        self._size += 1

    def dequeue(self):
        """Удалить и вернуть элемент из начала очереди."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self.capacity
        self._size -= 1
        return item

    def front(self):
        """Вернуть первый элемент без удаления."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data[self._front]

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self.capacity

    def size(self):
        return self._size

    def __str__(self):
        if self.is_empty():
            return "[]"
        items = []
        for i in range(self._size):
            idx = (self._front + i) % self.capacity
            items.append(str(self._data[idx]))
        return "[" + ", ".join(items) + "]"
class StackQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        """Добавить элемент в конец очереди."""
        self.stack_in.append(item)

    def _transfer(self):
        """Перенос элементов из stack_in в stack_out (если stack_out пуст)."""
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

    def dequeue(self):
        """Удалить и вернуть первый элемент очереди."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        self._transfer()
        return self.stack_out.pop()

    def front(self):
        """Вернуть первый элемент без удаления."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        self._transfer()
        return self.stack_out[-1]

    def is_empty(self):
        return not self.stack_in and not self.stack_out

    def size(self):
        return len(self.stack_in) + len(self.stack_out)

    def __str__(self):
        temp_out = list(reversed(self.stack_out))
        return "[" + ", ".join(map(str, temp_out + self.stack_in)) + "]"
if __name__ == "__main__":
    # Тест: CircularQueue
    print("=== CircularQueue ===")
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    print(cq)           # [1, 2]
    print("dequeue:", cq.dequeue())  # 1
    cq.enqueue(3)
    cq.enqueue(4)
    print(cq)           # [2, 3, 4]


    # Тест: StackQueue
    print("\n=== StackQueue ===")
    sq = StackQueue()
    sq.enqueue(10)
    sq.enqueue(20)
    sq.enqueue(30)
    print(sq)           # [10, 20, 30]
    print("dequeue:", sq.dequeue())  # 10
    sq.enqueue(40)
    print(sq)           # [20, 30, 40]
    print("front:", sq.front())      # 20