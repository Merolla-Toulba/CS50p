# get user input
orginal = input("Input: ")

# print first part
print("Output: ", end="")

# check for vowels and remove them
for c in orginal:
    match c:
        case "a" | "e" | "i" | "o" | "u":
            print("", end="")
        case "A" | "E" | "I" | "O" | "U":
            print("", end="")
        case _:
            print(f"{c}", end="")

print()
