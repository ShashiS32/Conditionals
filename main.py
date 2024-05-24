time = str(input("What time is it? ")).split(":")
x , y = time

if float(x) < 12:
    print("Breakfast")
elif float(x) <= 18 and float(y) <= 30:
    print("Lunch")
else:
    print("dinner")