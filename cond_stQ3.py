numbers=[]
x=0
while x!=5:
    num=input("Enter Any number :")
    numbers.append(num)
    x+=1
print(numbers)
max_value = max(numbers)
print("Max number = ",max_value)
min_value = min(numbers)
print("Min number = ",min_value)