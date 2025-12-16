import heapq
from typing import Any

class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._counter = 0

    def push(self, value: Any, priority: float):
        """Добавить элемент с приоритетом."""
        heapq.heappush(self._heap, (priority, self._counter, value))
        self._counter += 1

    def pop(self):
        """Извлечь элемент с минимальным приоритетом."""
        if self.is_empty():
            raise IndexError("pop from empty priority queue")
        priority, _, value = heapq.heappop(self._heap)
        return value

    def peek(self):
        """Посмотреть элемент с минимальным приоритетом (без извлечения)."""
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        return self._heap[0][2]

    def is_empty(self):
        return len(self._heap) == 0

    def size(self):
        return len(self._heap)

    def __str__(self):
        items = [(p, v) for p, _, v in self._heap]
        return str(items)
def task_scheduling_demo():
    print("=== Планирование задач ===")
    pq = PriorityQueue()

    tasks = [
        ("Обновить сервер", 3),
        ("Отправить email", 1),
        ("Сделать резервную копию", 2),
        ("Проверить логи", 3),
        ("Запустить тесты", 1),
    ]

    for task, priority in tasks:
        pq.push(task, priority)
        print(f"Добавлена задача: '{task}' с приоритетом {priority}")

    print("\nВыполнение задач по приоритету:")
    while not pq.is_empty():
        next_task = pq.pop()
        print(f" → Выполняется: {next_task}")
def k_smallest_with_pq(arr, k):
    pq = PriorityQueue()
    for x in arr:
        pq.push(x, x)
    return [pq.pop() for _ in range(min(k, pq.size()))]
import heapq

def k_smallest_optimized(arr, k):
    """Эффективный поиск k наименьших за O(n log k)."""
    if k <= 0:
        return []
    heap = []
    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, -num)
        else:
            if num < -heap[0]:
                heapq.heapreplace(heap, -num)
    return sorted(-x for x in heap)
print("\n=== Поиск k минимальных элементов ===")
arr = [10, 4, 3, 7, 8, 1, 9, 2, 5, 6]
k = 4

print(f"Массив: {arr}")
print(f"k = {k}")

result1 = k_smallest_with_pq(arr, k)
print(f"Через PriorityQueue: {result1}")

result2 = k_smallest_optimized(arr, k)
print(f"Оптимизированный способ: {result2}")

result3 = heapq.nsmallest(k, arr)
print(f"heapq.nsmallest: {result3}")