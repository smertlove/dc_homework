def main():
    freq = {}

    for word in input().split(", "):
        freq[word] = freq.get(word, 0) + 1

    for word, count in sorted(list(freq.items()), key=lambda c: c[1], reverse=True)[:3]:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
        