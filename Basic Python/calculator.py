# this method implement addintion of two number
def add(x,y):
    return x + y
# this method implement subtraction of two number
def subtract(x,y):
    return x -y
# this method implement multiplication of two number
def multiply(x,y):
    return x * y
# this method implement Division of two number 
def divide(x, y):
    # handled divide by zero exception
    try:
        return x/y
    except Exception:
        print("can't divide by zero")

# take input from the user
print("select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# take choice as user input
choice =input("Enter choice (1/2/3/4): ")

# take first number
num1 =int(input("Enter first Number:"))
# take second number
num2 =int(input("Enter Second Number:"))
# calling method according to chooice
if choice ==1:
    print(num1,"+",num2, add(num1,num2))
elif choice ==2:
    print(num1,"-",num2,subtract(num1,num2))
elif choice ==3:
    print(num1,"*",num2,multiply(num1,num2))
elif choice ==4:
    print(num1,"/",num2,divide(num1,num2))
else:
    print("Invalid Input")