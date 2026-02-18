def main():
    order = []
    final = 0.0

    while True:
        try:
            item = input("Item: ")
            order.append(item)
        except EOFError:
            break
        except KeyError:
            continue

    final = final_cost(order)
    print(f"Total: ${final:.2f}")


def final_cost(order):
    menu = {
        "baja taco": 4.25,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00
    }
    total = 0
    for item in order:
        total = total + menu[item.lower()]
    return total


if __name__ == "__main__":
    main()
