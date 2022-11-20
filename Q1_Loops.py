Original_List = [12, 75, 150, 180, 145, 525, 50]
numbers = []
for x in Original_List:
    if x > 150:
        if x > 500:
            break
        continue
    if x % 5 == 0:
        numbers.append(x)

print(numbers)