gender = input("Male/Female?").lower()
marital_status = input("Single/Married?").lower()
age = int(input("What's your age?"))
if marital_status == "Married":
    print("You can claim your insaurance")
else:
       if(gender == "male" and age > 30) or (gender == "female" and age >25 ):
           print("You can claim your insaurance")
       else:
            print("you cannot claim your insaurance")
    