import datetime

def gift_count(budget, month, birthdays):
    birthday_boys = [f"{boy} ({datetime.datetime.strftime(birthdays[boy], '%d.%m.%Y')})" for boy in birthdays if birthdays[boy].month == month]
    
    print(f"Именинники в месяце {month}: {', '.join(birthday_boys)}. При бюджете {budget} они получат по {budget // len(birthday_boys)} рублей.")
    

def main():
    birthdays = {"Иванов Иван Иванович": datetime.date(1989, 5, 1), "Петров Петр Петрович": datetime.date(1998, 5, 6)}

    gift_count(20000, 5, birthdays)

    gift_count(budget=20000, month=5, birthdays=birthdays)

if __name__ == "__main__":
    main()
