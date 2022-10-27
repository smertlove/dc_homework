import datetime

def gift_count(budget, month, birthdays):
    print(f"""Именинники в месяце {month}: {', '.join((birthday_boys := [f"{boy} ({datetime.datetime.strftime(bdate, '%d.%m.%Y')})" for boy, bdate in sorted(tuple(birthdays.items()), key=lambda c: c[1].day) if birthdays[boy].month == month]))}. При бюджете {budget} они получат по {budget // len(birthday_boys)} рублей.""" )


# def gift_count(budget, month, birthdays):    
    
#     birthday_boys = [f"{boy} ({datetime.datetime.strftime(bdate, '%d.%m.%Y')})" for boy, bdate in sorted(tuple(birthdays.items()), key=lambda c: c[1].day) if birthdays[boy].month == month]
    
#     if len(birthday_boys) == 0:
#         print("В этом месяце нет именниннков.")
#         return
    
#     print(f"""Именинники в месяце {month}: {', '.join(birthday_boys)}. При бюджете {budget} они получат по {budget // len(birthday_boys)} рублей.""")

def main():
    birthdays = {"Иванов Иван Иванович": datetime.date(1989, 5, 1), "Петров Петр Петрович": datetime.date(1998, 5, 6)}

    gift_count(20000, 5, birthdays)
    gift_count(20000, 5, {})

    gift_count(budget=20000, month=5, birthdays=birthdays)

if __name__ == "__main__":
    main()
