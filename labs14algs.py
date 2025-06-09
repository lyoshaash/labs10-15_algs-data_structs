class HashTable:
    def __init__(self, size=10 ** 6 + 3):
        self.size = size
        self.table = [[] for _ in range(size)]
    def _hash(self, key):
        return (key % self.size + self.size) % self.size
    def put(self, key, value):
        h = self._hash(key)
        for i, (k, v) in enumerate(self.table[h]):
            if k == key:
                self.table[h][i] = (key, value)
                return
        self.table[h].append((key, value))
    def get(self, key):
        h = self._hash(key)
        for k, v in self.table[h]:
            if k == key:
                return v
        return None
    def delete(self, key):
        h = self._hash(key)
        for i, (k, v) in enumerate(self.table[h]):
            if k == key:
                self.table[h].pop(i)
                return v
        return None

if __name__ == "__main__":
    n = int(input())
    ht = HashTable()

    for _ in range(n):
        parts = input().split()
        command = parts[0]
        key = int(parts[1])
        if command == "put":
            value = int(parts[2])
            ht.put(key, value)
        elif command == "get":
            res = ht.get(key)
            print("None" if res is None else res)
        elif command == "delete":
            res = ht.delete(key)
            print("None" if res is None else res)
