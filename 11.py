class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Вставить ключ в дерево."""
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        return node

    def search(self, key):
        """Проверить, содержится ли ключ в дереве."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node is not None
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        """Удалить ключ из дерева."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_min(node.right)
                node.key = successor.key
                node.right = self._delete_recursive(node.right, successor.key)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self):
        """In-order: лево → корень → право (возвращает отсортированный список)."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

    def preorder(self):
        """Pre-order: корень → лево → право."""
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.key)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder(self):
        """Post-order: лево → право → корень."""
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.key)

    def is_balanced(self):
        """
        Проверяет, сбалансировано ли дерево.
        Дерево сбалансировано, если для КАЖДОГО узла:
        |высота(лево) - высота(право)| ≤ 1
        """
        def check_height(node):
            if node is None:
                return 0

            left_height = check_height(node.left)
            if left_height == -1:
                return -1

            right_height = check_height(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        return check_height(self.root) != -1

    # Вспомогательный метод для отладки
    def height(self):
        """Высота дерева."""
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        return 1 + max(self._height_recursive(node.left), self._height_recursive(node.right))
if __name__ == "__main__":
    bst = BST()

    # Вставка
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25]
    for v in values:
        bst.insert(v)

    print("In-order (должен быть отсортирован):", bst.inorder())
    print("Pre-order:", bst.preorder())
    print("Post-order:", bst.postorder())

    # Поиск
    print("\nПоиск 40:", bst.search(40))
    print("Поиск 100:", bst.search(100))

    # Удаление
    print("\nДо удаления 30:", bst.inorder())
    bst.delete(30)
    print("После удаления 30:", bst.inorder())

    # Проверка баланса
    print("\nВысота дерева:", bst.height())
    print("Сбалансировано?", bst.is_balanced())

    # Пример НЕсбалансированного дерева
    print("\n--- Несбалансированное дерево ---")
    unbalanced = BST()
    for i in range(1, 8):
        unbalanced.insert(i)
    print("In-order:", unbalanced.inorder())
    print("Сбалансировано?", unbalanced.is_balanced())
