from datetime import date, timedelta

def main():
    d = date.fromisoformat("-".join(reversed(input().split("-"))))
    print((d - timedelta(d.weekday())).strftime("%d-%m-%Y"))

if __name__ == "__main__":
    main()
        