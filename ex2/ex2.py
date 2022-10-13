def main():
    digits = [0]

    while True:
        inp = input()

        if inp == "":
            break
        
        inp = int(inp)

        if inp % 2 == 0:
            digits.append(inp)

    print(sum(digits))
    


if __name__ == "__main__":
    main()
        