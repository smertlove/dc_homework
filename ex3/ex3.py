from functools import reduce

def get_balance(name, transactions):
    return sum((c["amount"] for c in transactions if c["name"] == name))

def count_debts(names, amount, transactions):
    return {name: ((debt := amount - get_balance(name, transactions)) > 0) * debt for  name in names}


def main():
    transactions = [ {"name": "Василий", "amount": 500}, {"name": "Петя", "amount": 100}, {"name": "Василий", "amount": -300}, ]

    print(get_balance("Василий", transactions))

    print(count_debts(["Василий", "Петя", "Вова"], 150, transactions))

if __name__ == "__main__":
    main()
