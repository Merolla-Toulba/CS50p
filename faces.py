def main():
    text = input()
    convert(text)


# changes :) & :( to actual emojis
def convert(str):
    words = str.split(" ")
    for word in words:
        if word == ":)":
            print("🙂 ", end="")
        elif word == ":(":
            print("🙁", end="")
        else:
            print(f"{word} ", end="")
    print()


main()
