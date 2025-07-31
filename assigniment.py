     # simple calculator
num1= float(input("enter the value of num1:"))
num2= float(input("Enter the value of num2:"))
operation= input("choose operation(*,+,/,-):")
if operation == "*":
    result= num1 * num2
elif operation == "+" :
    result= num1 + num2
elif operation == "-" :
    result= num1 - num2
elif operation == "/":
    # check for divisor
    if num2==0:
        print("MATH ERROR")
    else:
        result= num1/num2
else:
    print("The operation doesn't exist")
print(num1,operation,num2)
print("result:\n",result)