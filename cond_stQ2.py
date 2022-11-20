num1=input("Enter the first number :")
num1=int(num1)

print("1- +\n2- -\n3- *\n4- /\n5- ^\n6- %")
operating = input("Enter The operator : ")
num2=input("Enter the second number :")
num2=int(num2)
if operating =="1" or operating == "+":
    result=num1+num2
elif operating =="2" or operating == "-":
    result = num1-num2
elif operating =="3" or operating == "*":
    result = num1*num2
elif operating =="4" or operating == "/":
    result = num1/num2
elif operating =="5" or operating == "^":
    result = num1**num2
elif operating =="6" or operating == "%":
    result = num1%num2
print("The Result = ",result)
print("1- narrow approximity or to higher or less number \n2-Take the number without point\n3-Exit")
operating2=input(":")
if operating2=="1":
    result=round(result)
elif operating2=="2":
    result=int(result)
elif operating2=="3":
    result=exit()
print("The final result = :",result)