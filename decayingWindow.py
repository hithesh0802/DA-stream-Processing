from collections import defaultdict

def decaying_window(stream, decay=0.9):
    freq = defaultdict(float)

    for item in stream:
        for key in freq:
            freq[key] *= decay

        freq[item] += 1

    return max(freq, key=freq.get), freq


def main():
    stream = ["a", "b", "a", "c", "a", "b", "a"]

    most_freq, freq_map = decaying_window(stream)

    print("Most frequent (recent weighted):", most_freq)
    print("Scores:", dict(freq_map))

if __name__ == "__main__":
    main()