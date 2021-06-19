def lend_money(debts, person, amount):
    value = debts.get(person, 0)

    quantity = [amount]

    if value != 0:
        debts[person] = value + quantity

    else:
        debts[person] = quantity
    print(debts)

def amount_owed_by(debts, person):
    value = debts.get(person, [0])
    out = sum(value)
    return out

def total_amount_owed(debts):
    my_money = 0

    for values in debts.values():
        for numbers in values:
            my_money += numbers
    return my_money