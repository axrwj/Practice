import time
import re
from collections import Counter

class BadHashHashTable:
    def __init__(self, size=1000):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return 0

    def put(self, key, value):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return 0

    def increment(self, key):
        current = self.get(key)
        self.put(key, current + 1)
def good_hash_string(s: str, table_size: int) -> int:
    hash_val = 0
    base = 31
    for ch in s:
        hash_val = (hash_val * base + ord(ch)) % table_size
    return hash_val

class GoodHashHashTable:
    def __init__(self, size=1000):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return good_hash_string(key, self.size)

    def put(self, key, value):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return 0

    def increment(self, key):
        current = self.get(key)
        self.put(key, current + 1)
def preprocess_text(text: str):
    """Привести текст к нижнему регистру и извлечь слова (только буквы)."""
    text = text.lower()
    words = re.findall(r'[а-яa-z]+', text)
    return words

def count_frequencies_hashtable(words, hash_table_class):
    """Подсчитать частоты с использованием заданной хэш-таблицы."""
    ht = hash_table_class(size=10000)
    for word in words:
        if word:
            ht.increment(word)
    return ht

def get_top_10_from_hashtable(ht):
    """Извлечь топ-10 из хэш-таблицы."""
    all_items = []
    for bucket in ht.buckets:
        for k, v in bucket:
            all_items.append((k, v))
    all_items.sort(key=lambda x: (-x[1], x[0]))
    return all_items[:10]
sample_text = """
Once upon a time, in a land far, far away, there lived a wise old programmer.
The programmer wrote code in Python, C++, and JavaScript. He loved algorithms,
data structures, and clean code. He often said: "Choose the right structure for the task."
He used hash tables, arrays, linked lists, stacks, and queues. His favorite was the hash table.
"""

large_text = sample_text * 1000
words = preprocess_text(large_text)
def benchmark_hash_tables(words):
    print(f"Количество слов: {len(words)}\n")

    start = time.perf_counter()
    freq_bad = count_frequencies_hashtable(words, BadHashHashTable)
    time_bad = time.perf_counter() - start

    start = time.perf_counter()
    freq_good = count_frequencies_hashtable(words, GoodHashHashTable)
    time_good = time.perf_counter() - start


    start = time.perf_counter()
    freq_builtin = Counter(words)
    time_builtin = time.perf_counter() - start

    print(f"Время (плохая хэш-функция): {time_bad:.4f} сек")
    print(f"Время (хорошая хэш-функция): {time_good:.4f} сек")
    print(f"Время (встроенный dict/Counter): {time_builtin:.4f} сек")
    print(f"\nУскорение (плохая → хорошая): {time_bad / time_good:.1f}x")

    return freq_good
def benchmark_hash_tables(words):
    print(f"Количество слов: {len(words)}\n")


    start = time.perf_counter()
    freq_bad = count_frequencies_hashtable(words, BadHashHashTable)
    time_bad = time.perf_counter() - start


    start = time.perf_counter()
    freq_good = count_frequencies_hashtable(words, GoodHashHashTable)
    time_good = time.perf_counter() - start


    start = time.perf_counter()
    freq_builtin = Counter(words)
    time_builtin = time.perf_counter() - start

    print(f"Время (плохая хэш-функция): {time_bad:.4f} сек")
    print(f"Время (хорошая хэш-функция): {time_good:.4f} сек")
    print(f"Время (встроенный dict/Counter): {time_builtin:.4f} сек")
    print(f"\nУскорение (плохая → хорошая): {time_bad / time_good:.1f}x")

    return freq_good
def print_top_10(freq_table):
    top10 = get_top_10_from_hashtable(freq_table)
    print("\nТоп-10 самых частых слов:")
    print("-" * 25)
    for i, (word, count) in enumerate(top10, 1):
        print(f"{i:2}. {word:<15} — {count}")
if __name__ == "__main__":
    large_text = sample_text * 1000
    words = preprocess_text(large_text)

    freq_table = benchmark_hash_tables(words)

    print_top_10(freq_table)