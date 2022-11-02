import os

def popular_name_from_generator(data):
    freq = {}
    temp_max = 0  ## чтобы не искать максимум лишний раз
    for elem in data:
        freq[elem] = freq.pop(elem, 0) + 1
        if temp_max < freq[elem]:
            temp_max = freq[elem]
    return ', '.join(sorted([k for k in freq if freq[k] == temp_max]))

def get_popular_name_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = map(lambda c: c.split()[0], file.read().strip().split('\n'))
    return popular_name_from_generator(data)


def main():
    test_dir = os.path.join( os.path.dirname(__file__), "tests" )
    test_paths = ["1.txt", "2.txt", "3.txt"]
    for path in  test_paths:
        print(f"{path}:\n")
        print(get_popular_name_from_file(os.path.join(test_dir, path)))
        print("- - - - -\n")


if __name__ == "__main__":
    main()
