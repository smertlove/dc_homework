import os
import re


def check_telnum(string):
    pattern = re.compile(r"^(8[-\s]?|\+?7[-\s]?)?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}$")
    return pattern.match(string) is not None


def check_eml(string):
    pattern = re.compile(r"^[\w\.]+@[\w\.]+\.\w\w+$")
    return pattern.match(string) is not None


def check_string(string):
    return check_telnum(string) or check_eml(string)


def main():
    test_dir = os.path.join(os.path.dirname(__file__), "tests")
    test_paths = [
        "good_numbers.txt",
        "bad_numbers.txt",
        "good_emls.txt",
        "bad_emls.txt",
    ]

    for path in test_paths:
        print(f"{path}:\n")
        with open(os.path.join(test_dir, path), encoding='utf-8') as test_file:
            for case in test_file:
                print(case.strip(), '\t', check_string(case.strip()))
        print("- - - - -\n")


if __name__ == "__main__":
    main()
