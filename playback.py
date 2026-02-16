# gets user input
text = input("")

# divides text based on spaces
string = text.split(" ")

iterations = len(string)

# prints ... between all words
for i in range(iterations - 1):
    print(f"{string[i]}...", end="")

print(f"{string[iterations - 1]}")
