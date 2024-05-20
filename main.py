answer = input("What is the Answer to the universe Great Question of Life, the Universe, and Everything? ").lower()

if answer.isdigit() and int(answer) == 42:
    print("Yes")
elif answer == "forty two" or answer == "forty-two":
    print("Yes")
else:
    print("No")
