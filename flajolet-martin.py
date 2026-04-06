def count_trailing_zeros(x):
    count = 0
    while x > 0 and x % 2 == 0:
        count += 1
        x //= 2
    return count


def flajolet_martin(stream):
    max_zeros = 0

    for x in stream:
        h = (x * 13) % 32  

        zeros = count_trailing_zeros(h)
        max_zeros = max(max_zeros, zeros)

        print(f"Element: {x}, Hash: {h}, Trailing zeros: {zeros}")

    return 2 ** max_zeros


def main():
    stream = [1, 2, 3, 2, 1, 4, 5, 6, 5]

    estimate = flajolet_martin(stream)
    print("Estimated distinct count:", estimate)

if __name__ == "__main__":
    main()