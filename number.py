try:
    raw = input("What is the value of X?")
    x = int(raw)
    print(f"the value of x is {x}")
except ValueError:
    print(f"You fool {raw} isn't any integer")