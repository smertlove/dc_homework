import json


def mean_age(json_string):
    ages = [obj["age"] for obj in json.loads(json_string)]
    return json.dumps({"mean_age": sum(ages)/len(ages)})


def main():
    testcase = '''[
    {
        "name": "Петр",
        "surname": "Петров",
        "patronymic": "Васильевич",
        "age": 23,
        "occupation": "ойтишнек"
    },
    {
        "name": "Василий",
        "surname": "Васильев",
        "patronymic": "Петрович",
        "age": 24,
        "occupation": "дворник"
    }
]'''
    print(mean_age(testcase))


if __name__ == "__main__":
    main()
