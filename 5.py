class ArrayStack:
    def __init__(self):
        self._data = []

    def push(self, item):
        """Добавить элемент на вершину стека."""
        self._data.append(item)

    def pop(self):
        """Удалить и вернуть элемент с вершины стека."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def top(self):
        """Вернуть верхний элемент без удаления."""
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)
class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class LinkedStack:
    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, item):
        """Добавить элемент на вершину стека."""
        new_node = ListNode(item, self._head)
        self._head = new_node
        self._size += 1

    def pop(self):
        """Удалить и вернуть элемент с вершины стека."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self._head.value
        self._head = self._head.next
        self._size -= 1
        return value

    def top(self):
        """Вернуть верхний элемент без удаления."""
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self._head.value

    def is_empty(self):
        return self._head is None

    def size(self):
        return self._size
def is_valid_parentheses(s: str, stack_impl=ArrayStack) -> bool:
    """
    Проверяет, является ли строка s корректной скобочной последовательностью.
    Параметр stack_impl позволяет выбрать реализацию стека (по умолчанию — массив).
    """
    stack = stack_impl()
    matching = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty():
                return False
            top = stack.pop()
            if top != matching[char]:
                return False

    return stack.is_empty()
# Тесты
test_cases = [
    ("()", True),
    ("()[]{}", True),
    ("([{}])", True),
    ("(]", False),
    ("([)]", False),
    ("{[()]}", True),
    ("", True),
    ("(((", False),
    ("{{{}}}", True),
]

print("Проверка с ArrayStack:")
for s, expected in test_cases:
    result = is_valid_parentheses(s, ArrayStack)
    print(f"{s:10} → {result} (ожидалось {expected}) → {'✅' if result == expected else '❌'}")

print("\nПроверка с LinkedStack:")
for s, expected in test_cases:
    result = is_valid_parentheses(s, LinkedStack)
    print(f"{s:10} → {result} (ожидалось {expected}) → {'✅' if result == expected else '❌'}")