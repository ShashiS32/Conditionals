answ = input("camelCase: ")

for letter in answ:
    if letter.isupper():
        print("_" + letter.lower(), end="")

    else:
        print(letter, end="")