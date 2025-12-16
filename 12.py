class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word_count = 0
        self.prefix_count = 0
class AdvancedTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        """
        Вставить слово в Trie.
        Увеличивает word_count и prefix_count для всех узлов на пути.
        """
        word = word.lower().strip()
        if not word:
            return
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
        node.is_end = True
        node.word_count += 1

    def search(self, word: str) -> bool:
        """
        Проверить, существует ли слово в Trie (хотя бы один раз).
        """
        node = self._get_node(word)
        return node is not None and node.is_end

    def count_words_with_prefix(self, prefix: str) -> int:
        """
        Вернуть количество слов, начинающихся с данного префикса.
        Сложность: O(m), где m = длина префикса.
        """
        node = self._get_node(prefix)
        return node.prefix_count if node else 0

    def count_occurrences(self, word: str) -> int:
        """
        Вернуть, сколько раз слово было вставлено.
        """
        node = self._get_node(word)
        return node.word_count if node and node.is_end else 0

    def _get_node(self, prefix: str):
        """
        Вспомогательный метод: вернуть узел, соответствующий префиксу.
        """
        prefix = prefix.lower().strip()
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def delete(self, word: str) -> bool:
        """
        Удалить одно вхождение слова.
        Если слово вставлено несколько раз — уменьшает word_count.
        Если word_count становится 0 — удаляет узлы, если они больше не нужны.
        Возвращает True, если слово было найдено и удалено (хотя бы частично).
        """
        word = word.lower().strip()
        if not word:
            return False

        def _delete_recursive(node, word, index):
            if index == len(word):
                # Достигли конца слова
                if not node.is_end:
                    return False, node
                node.word_count -= 1
                if node.word_count == 0:
                    node.is_end = False
                should_delete = not node.is_end and len(node.children) == 0
                return True, node if not should_delete else None

            char = word[index]
            if char not in node.children:
                return False, node

            child_node = node.children[char]
            deleted, new_child = _delete_recursive(child_node, word, index + 1)

            if not deleted:
                return False, node

            # Обновляем ребёнка
            if new_child is None:
                del node.children[char]
                node.prefix_count -= 1
                should_delete_current = not node.is_end and len(node.children) == 0
                return True, node if not should_delete_current else None
            else:
                return True, node

        success, _ = _delete_recursive(self.root, word, 0)
        return success
if __name__ == "__main__":
    trie = AdvancedTrie()

    words = ["apple", "app", "application", "app", "banana", "ban", "band"]
    for w in words:
        trie.insert(w)

    print("Слово 'app' существует?", trie.search("app"))
    print("Слово 'orange' существует?", trie.search("orange"))

    print("\nКоличество вхождений:")
    print("'app':", trie.count_occurrences("app"))
    print("'apple':", trie.count_occurrences("apple"))

    print("\nКоличество слов по префиксам:")
    print("Префикс 'app':", trie.count_words_with_prefix("app"))
    print("Префикс 'ban':", trie.count_words_with_prefix("ban"))
    print("Префикс 'band':", trie.count_words_with_prefix("band"))
    print("Префикс 'xyz':", trie.count_words_with_prefix("xyz"))

    # Удаление
    print("\nУдаляем одно вхождение 'app'...")
    trie.delete("app")
    print("'app' осталось:", trie.count_occurrences("app"))
    print("Префикс 'app' теперь:", trie.count_words_with_prefix("app"))

    print("Удаляем 'apple'...")
    trie.delete("apple")
    print("Слово 'apple' существует?", trie.search("apple"))
    print("Префикс 'app' теперь:", trie.count_words_with_prefix("app"))

    # Попытка удалить несуществующее слово
    print("Удаление 'orange' успешна?", trie.delete("orange"))
