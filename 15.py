class MinHeap:
    def __init__(self, array=None):
        """
        Инициализация кучи.
        Если передан массив — строим кучу за O(n).
        Иначе создаём пустую.
        """
        if array is not None:
            self.heap = array[:]
            self._heapify()
        else:
            self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_up(self, i):
        """Подъём элемента вверх до восстановления свойств кучи."""
        while i > 0:
            parent = self._parent(i)
            if self.heap[parent] <= self.heap[i]:
                break
            self._swap(i, parent)
            i = parent

    def _sift_down(self, i):
        """Спуск элемента вниз до восстановления свойств кучи."""
        n = len(self.heap)
        while True:
            smallest = i
            left = self._left(i)
            right = self._right(i)

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            self._swap(i, smallest)
            i = smallest

    def insert(self, value):
        """Вставка элемента. Сложность: O(log n)."""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)
        assert self.is_valid(), "Heap property violated after insert!"

    def extract_min(self):
        """Извлечение минимума. Сложность: O(log n)."""
        if not self.heap:
            raise IndexError("extract_min from empty heap")
        if len(self.heap) == 1:
            min_val = self.heap.pop()
        else:
            min_val = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._sift_down(0)
        assert self.is_valid(), "Heap property violated after extract_min!"
        return min_val

    def _heapify(self):
        """Построение кучи из массива за O(n)."""
        n = len(self.heap)
        for i in range((n // 2) - 1, -1, -1):
            self._sift_down(i)
        assert self.is_valid(), "Heap property violated after heapify!"

    def is_valid(self):
        """Проверка свойств мин-кучи."""
        n = len(self.heap)
        for i in range(n):
            left = self._left(i)
            right = self._right(i)
            if left < n and self.heap[i] > self.heap[left]:
                return False
            if right < n and self.heap[i] > self.heap[right]:
                return False
        return True

    def size(self):
        return len(self.heap)

    def peek(self):
        """Посмотреть минимум без извлечения."""
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def __str__(self):
        return str(self.heap)
if __name__ == "__main__":
    print("=== 1. Создание кучи из массива ===")
    arr = [10, 3, 5, 1, 8, 2]
    print("Исходный массив:", arr)
    heap = MinHeap(arr)
    print("Куча после heapify:", heap)
    print("Корректна?", heap.is_valid())

    print("\n=== 2. Вставка элементов ===")
    for x in [0, 4, -1]:
        heap.insert(x)
        print(f"Вставлено {x} → куча: {heap}")

    print("\n=== 3. Извлечение минимума ===")
    while heap.size() > 0:
        min_val = heap.extract_min()
        print(f"Извлечено: {min_val}, остаток: {heap}")

    print("\n=== 4. Построение кучи из случайного массива ===")
    import random
    random.seed(42)
    big_arr = [random.randint(1, 100) for _ in range(20)]
    print("Случайный массив:", big_arr[:10], "...")
    big_heap = MinHeap(big_arr)
    print("Куча построена. Корректна?", big_heap.is_valid())
    print("Минимум:", big_heap.peek())