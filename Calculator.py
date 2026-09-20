print("Pls select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Average")

select = input("Enter your choice (1/2/3/4/5): ")
Number1=int(input("Enter first number: "))
Number2=int(input("Enter second number: "))


sum = Number1 + Number2
Sub = Number1 - Number2
Mul = Number1 * Number2
Div = Number1 / Number2
Avg = (Number1 + Number2) / 2


if select == '1':
    print("the sum of the given two digits is: ", sum)
elif select == '2':
    print("the difference of the given two digits is: ", Sub)
elif select == '3':
    print("the product of the given two digits is: ", Mul)
elif select == '4':
    print("the division of the given two digits is: ", Div)
elif select == '5':
    print("the average of the given two digits is: ", Avg)
else:
    print("Invalid input!!, please select a valid operation.")



