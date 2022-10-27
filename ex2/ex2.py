from functools import reduce

def lists_sum(*lists, unique=False) :

    # if unique:
    #     return sum(
    #         reduce(
    #             lambda st1, st2: st1 | st2,
    #              map(set, [*lists, [0]])
    #              )
    #         )

    # return sum([sum(list) for list in [*lists, [0]]])
    return (sum(reduce(lambda st1, st2: st1 | st2,map(set, [*lists, [0]])))if unique else sum([sum(list) for list in [*lists, [0]]])) if len(lists) > 0 else 0 

def main():
    
    print(lists_sum([1, 1], [1], [1, 2, 3]))

    print(lists_sum([1, 1, 1], [1, 1], unique=True))

    print(lists_sum([1, 1, 1], unique=False))
    print(lists_sum( unique=False))
    print(lists_sum([], [], [], unique=False))

if __name__ == "__main__":
    main()
