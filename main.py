
# author : Nanae Shimoi

#【theme】-----------------
#Judge the grades entered by the user as A,B,C,D or F

#【step】-------------------
#1,ask "Please enter your grade percentage:"
#2,initial setup
#3,grades to variables
#4,desplay the A,B,C,D or F
#5,desplay "pass or not"

#【to do list】-------------
#1,use "percentage=float(input""")"--------ask "Please enter your grade percentage:"
#2,use "error"-------initial setup
#3,use "if percentage>=90: , elif percentage>=80:,70:,60:"--------grades to variables
#4,use "print(f"Your grade is :{}")"--------desplay the A,B,C,D or F
#5,use"if percentage >= 70:print(""),else:"---------desplay "pass or not"

#【assignment】--------------
percentage = float(input("Please enter your grade percentage:"))

if percentage >= 90: 
        letter = "A"
elif percentage >= 80:
        letter = "B"
elif percentage >= 70:
        letter = "C"
elif percentage >= 60:
        letter = "D"
else :
        letter = "F"

print(f"Your grade is: {letter}")

if percentage >= 70:
        print("Congratulation! You passed the class.")
else: 
        print("Do not give up! Try again next time.")
