class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class AutocompleteTrie:
    def __init__(self):
        self.root = TrieNode()
        self.word_freq = {}

    def insert(self, word: str, freq: int = 1):
        """
        Вставить слово в Trie и обновить его частоту в HashMap.
        Если слово уже есть — увеличить частоту.
        """
        word = word.lower().strip()
        if not word:
            return

        self.word_freq[word] = self.word_freq.get(word, 0) + freq

        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def _find_prefix_node(self, prefix: str):
        """
        Найти узел, соответствующий префиксу.
        Возвращает узел или None, если префикс не найден.
        """
        prefix = prefix.lower().strip()
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def _collect_all_words(self, node: TrieNode, prefix: str):
        """
        Рекурсивно собрать все слова, начинающиеся с `prefix`.
        Возвращает список слов.
        """
        results = []
        if node.is_end_of_word:
            results.append(prefix)

        for char, child_node in node.children.items():
            results.extend(self._collect_all_words(child_node, prefix + char))
        return results

    def autocomplete(self, prefix: str, limit: int = 10):
        """
        Вернуть до `limit` слов с данным префиксом,
        отсортированных по убыванию частоты.
        """
        prefix = prefix.lower().strip()
        if not prefix:
            return []

        prefix_node = self._find_prefix_node(prefix)
        if not prefix_node:
            return []

        all_words = self._collect_all_words(prefix_node, prefix)

        all_words.sort(key=lambda word: (-self.word_freq[word], word))

        return all_words[:limit]
if __name__ == "__main__":
    # Создаём автокомплитер
    ac = AutocompleteTrie()

    words_with_freq = [
        ("apple", 50),
        ("application", 30),
        ("apply", 20),
        ("appreciate", 10),
        ("approach", 25),
        ("banana", 60),
        ("band", 15),
        ("bandana", 5),
        ("cat", 40),
        ("car", 35),
        ("card", 20),
        ("care", 18),
        ("careful", 12),
        ("app", 5),
    ]

    for word, freq in words_with_freq:
        ac.insert(word, freq)

    test_prefixes = ["app", "ban", "car", "ca", "zoo"]

    for prefix in test_prefixes:
        suggestions = ac.autocomplete(prefix, limit=5)
        print(f"\nPrefix: '{prefix}'")
        print("Suggestions:")
        for word in suggestions:
            print(f"  {word} (freq: {ac.word_freq[word]})")
