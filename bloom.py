class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.bits = [0] * size

    #use multiple hash functions to reduce false positives

    def hash1(self, x):
        return x % self.size

    def hash2(self, x):
        return (x * 7) % self.size

    def hash3(self, x):
        return (x * 11) % self.size

    def get_hashes(self, x):
        return [self.hash1(x), self.hash2(x), self.hash3(x)]

    def add(self, x):
        for h in self.get_hashes(x):
            self.bits[h] = 1

    def check(self, x):
        for h in self.get_hashes(x):
            if self.bits[h] == 0:
                return False
        return True


def main():
    bf = BloomFilter(20)

    stream = [1, 2, 3, 4, 5]
    for x in stream:
        bf.add(x)

    test = [3, 7]
    for t in test:
        print(f"{t} present? ->", bf.check(t))

if __name__ == "__main__":
    main()