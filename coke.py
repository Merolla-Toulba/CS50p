def main():
    # print initial amount
    print("Amount Due: 50")
    amount = 50

    # loop to iterate how much is left
    while True:
        # end if zero is reached and print amount owed
        if amount == 0:
            print("Change Owed: 0")
            break
        # end if we go below zero and tell the user how much change theyll get
        elif amount <= 0:
            print(f"Change Owed: {amount * -1}")
            break
        # print to the user how much is left to pay
        else:
            coin_input = int(input("Insert Coin: ").strip())
            coin_input = calc(amount, coin_input)
            print(f"Amount Due: {coin_input}")
            amount = coin_input


# calculate how much is left after inserting coin
def calc(amount, coin):
    total = amount
    if coin == 25:
        return total - 25
    elif coin == 10:
        return total - 10
    elif coin == 5:
        return total - 5
    else:
        return total


if __name__ == "__main__":
    main()
