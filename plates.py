# get user input and print validation
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# checks if all plate conditions are meet
def is_valid(s):
    if letter_start(s) and max_no(s) and is_punc(s) and number_ending(s) and zero_start(s):
        return True
    else:
        return False


# checks if the first 2 letters are letters
def letter_start(s):
    return s[0:2].isalpha()


# checks if the number of characters in the plate is between 2 and 6
def max_no(s):
    return 2 <= len(s) <= 6


# looks for special characters and returns false if so
def is_punc(s):
    return s.isalnum()


# checks if the ending is number followed by a letter
def number_ending(s):
    if s[-2:-1].isalpha() and s[-1:].isdigit():
        return False
    elif s[-2:-1].isdigit() and s[-1:].isalpha():
        return False
    else:
        return True


# checks if the first number present is 0 and returns false if so
def zero_start(s):
    for c in s:
        if c.isdigit():
            if c == "0":
                return False
            else:
                return True
    return True


if __name__ == "__main__":
    main()
