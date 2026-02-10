Score= int(input("Score: "))
def Grade_card():
 if  Score >= 90 :
    print("Grade: A")
 elif Score >= 80:
    print("Grade: B")
 elif Score >= 70:
    print("Grade: c")
 elif Score >=60 :
    print("Grade: D")
 else: 
    print("Grade: E")
if  0 <= Score <= 100:
   Grade_card()
else:
   print("Enter the correct Scores")