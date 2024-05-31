amount_due = 50

while amount_due > 0:
    resp = int(input(f"Amount Due: {amount_due}\nInsert Coin: "))
    amount_due -= resp

if amount_due == 0:
    print("Change Owed: 0")
elif amount_due < 0:
    change_owed = abs(amount_due) 
    print(f"Change Owed: {change_owed}")
