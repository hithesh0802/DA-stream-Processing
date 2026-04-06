import random

def ams(stream):
    n = len(stream)
    i = random.randint(0, n - 1)
    x = stream[i]

    count = sum(1 for j in range(i, n) if stream[j] == x)

    return n * (2 * count - 1)


def main():
    stream = [1, 2, 2, 3, 3, 3, 4]

    estimate = ams(stream)
    print("Estimated F2:", estimate)

if __name__ == "__main__":
    main()