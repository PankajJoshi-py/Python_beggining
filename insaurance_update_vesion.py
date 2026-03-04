def main():

    while True:
        gender = input("Male/Female? ").lower()
        if gender in ["male", "female"]:
            break
        print("Invalid gender. Try again.\n")

 
    while True:
        marital_status = input("Single/Married? ").lower()
        if marital_status in ["single", "married"]:
            break
        print("Invalid marital status. Try again.\n")

    if marital_status == "married":
        print("You can claim your insurance")
        return


    while True:
        try:
            age = int(input("What's your age? "))
            if 0 < age < 150:
                break
            else:
                print("Enter realistic age.\n")
        except ValueError:
            print("Age must be an integer.\n")

    if (gender == "male" and age > 30) or (gender == "female" and age > 25):
        print("You can claim your insurance")
    else:
        print("You cannot claim your insurance")

main()