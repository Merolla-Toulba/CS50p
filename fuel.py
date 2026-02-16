equation = input("Fraction: ").strip()

try:
    x,y = equation.split("/")
    final = round((int(x) / int(y)) * 100)
    if 0 > final or final > 100:
        raise ValueError
except (ValueError, ZeroDivisionError):
    equation = input("Fraction: ").strip()
else:
    if final <= 1:
        print("E")
    elif final >= 99:
        print("F")
    else:
        print(f"{final}%")

