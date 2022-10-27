from functools import reduce

def get_balance(name, transactions):
    return sum((c["amount"] for c in transactions if c["name"] == name))

def count_debts(names, amount, transactions):
    answ = {name: amount - get_balance(name, transactions) for  name in names}
    for name in answ:
        if answ[name] < 0:
            answ[name] = 0
    return answ


def main():
    transactions = [ {"name": "Василий", "amount": 500}, {"name": "Петя", "amount": 100}, {"name": "Василий", "amount": -300}, ]

    print(get_balance("Василий", transactions))

    print(count_debts(["Василий", "Петя", "Вова"], 150, transactions))

if __name__ == "__main__":
    main()
