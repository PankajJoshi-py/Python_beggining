name = input("Enter your name : ")
match name:
    case  "Harry" | "Muskan" | "hermione" | "Ron":
        print("gryffion")
    case "padma":
        print("Slythrine")
    case _:
        print("Who?")