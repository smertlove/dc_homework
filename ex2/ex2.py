from functools import reduce

def lists_sum(*lists, unique=False) :
    if unique:
        return sum(reduce(lambda st1, st2: st1 | st2, map(set, lists)))
    return sum([sum(list) for list in lists])

def main():
    
    print(lists_sum([1, 1], [1], [1, 2, 3]))

    print(lists_sum([1, 1, 1], [1, 1], unique=True))

    print(lists_sum([1, 1, 1], unique=False))

if __name__ == "__main__":
    main()
