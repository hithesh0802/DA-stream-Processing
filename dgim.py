class DGIM:
    def __init__(self, window_size):
        self.window_size = window_size
        self.buckets = []
        self.time = 0

    def add(self, bit):
        self.time += 1

        if bit == 1:
            self.buckets.insert(0, (1, self.time))

        i = 0
        while i < len(self.buckets) - 2:
            if self.buckets[i][0] == self.buckets[i+1][0] == self.buckets[i+2][0]:
                size = self.buckets[i][0]
                self.buckets.pop(i+2)
                self.buckets[i+1] = (size*2, self.buckets[i+1][1])
            else:
                i += 1

        self.buckets = [(s, t) for (s, t) in self.buckets if self.time - t < self.window_size]

    def count(self):
        total = 0
        for i in range(len(self.buckets)):
            if i == len(self.buckets) - 1:
                total += self.buckets[i][0] // 2
            else:
                total += self.buckets[i][0]
        return total


def main():
    dgim = DGIM(5)

    stream = [1, 0, 1, 1, 0, 1, 1]

    for bit in stream:
        dgim.add(bit)

    print("Estimated 1's in last window:", dgim.count())

if __name__ == "__main__":
    main()