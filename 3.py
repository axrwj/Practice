class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def pushFront(self, value):
        """
        Сложность: O(1)
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pushBack(self, value):
        """
        Сложность: O(n)
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def find(self, value):
        """
        Сложность: O(n)
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def remove(self, value):
        """
        Сложность: O(n)
        """
        if self.head is None:
            return False


        if self.head.value == value:
            self.head = self.head.next
            return True


        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next is None:
            return False

        current.next = current.next.next
        return True

    def reverse(self):
        """
        Сложность: O(n)
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) if values else "Empty list"
lst = LinkedList()
lst.pushBack(1)
lst.pushBack(2)
lst.pushFront(0)
print(lst)  # 0 -> 1 -> 2

lst.remove(1)
print(lst)  # 0 -> 2

print(lst.find(2))  # True
print(lst.find(5))  # False

lst.reverse()
print(lst)  # 2 -> 0