
def calculator(first, second, op):
    if op == "sum":
        print("sum =", first + second)
    if op == "min":
        print("min =", first - second)

first = int(input("first number: "))
second = int(input("second num  ber: ") )
calculator(first, second, "min")
