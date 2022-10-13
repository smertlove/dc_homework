def main():
    print(*sorted(map(int, [int(input()) for _ in range(5)]), reverse=True), sep="\n")

if __name__ == "__main__":
    main()
        