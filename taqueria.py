def main():
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

    total = 0.0
    while True:
        try:
            item = input("Item: ").strip().lower()
        except EOFError:
            print()
            break

        if item in menu:
            total += menu[item]
            print(f"Total: ${total:.2f}")
        else:
            continue


if __name__ == "__main__":
    main()

""" this was edited with the help of chatgpt because the cs50 duck wasnt responsive and kept asking the same question over and over
in 3 *seperate* chats after i repeatedly said that was not the problem [i was sure it wasnt] so yeah just wanted to put this out there

this was my original code but check50 always rejected it because you had to enter before control d [i didnt work at all with the same line text]
and i couldnt find a better way anywhere online so i resorted to printing the total after each iteration so that check50 accepts it
Im not sure how well this works with the academic honesty but here it is. I've spent a month on this with no avail so i went to gpt cuz it got annoying
so yeah thats the story sorry if its kinda of a rant :)

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
    print(f"\rTotal: ${final:.2f}")


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
"""
