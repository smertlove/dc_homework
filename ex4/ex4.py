def main():
    string = input()
    substring = input()

    print(*[word for word in string.split() if substring.lower() in word.lower()], sep="\n")

if __name__ == "__main__":
    main()
        