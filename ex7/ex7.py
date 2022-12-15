def main():
    print(*sorted(set(input().lower().split(", "))), sep=", ")

if __name__ == "__main__":
    main()