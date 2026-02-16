import emoji

input = input("Input: ")

if "_" in input:
    output = emoji.emojize(input)
    print(f"Output: {output}")
else:
    output = emoji.emojize(input, language='alias')
    print(f"Output: {output}")
