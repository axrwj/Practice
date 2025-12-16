class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"Node({self.value})"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pushBack(self, value):
        """Вспомогательный метод: добавить в конец."""
        new_node = Node(value)
        if self.tail is None:  # список пуст
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pushFront(self, value):
        """Вспомогательный метод: добавить в начало."""
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertAfter(self, node, value):
        """
        Вставка нового узла со значением `value` ПОСЛЕ указанного `node`.
        Требуется, чтобы `node` принадлежал списку.
        Сложность: O(1)
        """
        if node is None:
            raise ValueError("Node cannot be None")

        new_node = Node(value)
        new_node.next = node.next
        new_node.prev = node

        if node.next:
            node.next.prev = new_node
        else:
            self.tail = new_node

        node.next = new_node

    def deleteNode(self, node):
        """
        Удаление указанного узла из списка.
        Требуется, чтобы `node` принадлежал списку.
        Сложность: O(1)
        """
        if node is None:
            raise ValueError("Node cannot be None")

        if node.prev:
            node.prev.next = node.next
        else:
            # node — это head
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev = None
        node.next = None

    def find(self, value):
        """
        Сложность: O(n)
        """
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        return " <-> ".join(str(val) for val in self)
if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.pushBack(10)
    dll.pushBack(20)
    dll.pushBack(30)

    print("Исходный список:", dll)  # 10 <-> 20 <-> 30

    node_20 = dll.find(20)
    if node_20:
        dll.insertAfter(node_20, 25)
        print("После вставки 25:", dll)  # 10 <-> 20 <-> 25 <-> 30

        dll.deleteNode(node_20)
        print("После удаления 20:", dll)  # 10 <-> 25 <-> 30

    print("Элементы через for:")
    for val in dll:
        print(val)

    # Вывод:
    # 10
    # 25
    # 30