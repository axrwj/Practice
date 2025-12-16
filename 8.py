def hash_string(s: str, table_size: int) -> int:
    """
    Полиномиальный хэш для строки.
    База = 31, модуль = table_size.
    """
    if table_size <= 0:
        raise ValueError("Table size must be positive")
    hash_val = 0
    base = 31
    for char in s:
        hash_val = (hash_val * base + ord(char)) % table_size
    return hash_val
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self._count = 0

    def _hash(self, key):
        if not isinstance(key, str):
            raise TypeError("Only string keys are supported")
        return hash_string(key, self.size)

    def put(self, key: str, value):
        """Вставить или обновить пару (key, value)."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self._count += 1

    def get(self, key: str):
        """Получить значение по ключу. Возвращает None, если ключа нет."""
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key: str) -> bool:
        """Удалить ключ. Возвращает True, если удалён, иначе False."""
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._count -= 1
                return True
        return False

    def visualize(self):
        """Визуализация состояния хэш-таблицы."""
        print(f"\nHash Table (size={self.size}, count={self._count}):")
        print("-" * 50)
        for i, bucket in enumerate(self.buckets):
            if bucket:
                items = ", ".join([f"'{k}': {v}" for k, v in bucket])
                print(f"Bucket {i:2}: [{items}]")
            else:
                print(f"Bucket {i:2}: [EMPTY]")
        print("-" * 50)

    def __str__(self):
        pairs = []
        for bucket in self.buckets:
            for k, v in bucket:
                pairs.append(f"'{k}': {v}")
        return "{" + ", ".join(pairs) + "}"
if __name__ == "__main__":
    ht = HashTable(size=7)

    data = [
        ("яблоко", 10),
        ("банан", 20),
        ("вишня", 30),
        ("груша", 40),
        ("дыня", 50),
        ("ежевика", 60),
        ("инжир", 80),
    ]

    for key, value in data:
        ht.put(key, value)
        print(f"Вставлено: {key} → {value}")

    ht.visualize()

    # Проверка get
    print("\nПроверка значений:")
    print("Банан:", ht.get("банан"))
    print("Апельсин:", ht.get("апельсин"))

    # Удаление
    ht.remove("вишня")
    print("\nПосле удаления 'вишня':")
    ht.visualize()