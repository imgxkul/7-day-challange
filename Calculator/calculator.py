number_1 = int(input("Enter A Number: "))
operator = input("Enter an Operator: ")
number_2 = int(input("Enter Another Number: "))
if operator == "+" or operator == "-" or operator == "/" or operator == "*":
 print("Answer = ",eval(f"{number_1}{operator}{number_2}"))
else:
 print("Invalid Operator")
