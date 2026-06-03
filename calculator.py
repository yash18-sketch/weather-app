print("BASIC CALCULATOR")
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice: ")

if  choice == '1':
          print( "addition=",  num1+num2)

elif choice == '2':
          print("substraction=",num1-num2)

elif choice ==  '3':
        print("multiplication= ", num1*num2)

elif choice == '4':
        print("multiplication=", num1/num2)


else:
            print("Invalid choice")
