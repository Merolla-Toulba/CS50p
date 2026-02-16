def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollar):
    amount = dollar.replace("$", "")
    amount = float(amount)
    return amount


def percent_to_float(percent):
    decimal = percent.replace("%", "")
    decimal = int(decimal) / 100
    return decimal


main()
