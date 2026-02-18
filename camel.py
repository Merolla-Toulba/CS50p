camelcase = input("camelCase: ").strip()

# print first part
print("snake_case: ", end="")

# change from camelcase to snakecase letter by letter
for c in camelcase:
    if c.isupper():
        print(f"_{c.lower()}", end="")
    else:
        print(f"{c}", end="")
print()
