a = [1,2,3,4,5,6,7,8,9]
element = int(input("Enter Number to find its position:"))
position = -1

for i in range(len(a)):
    # print(i)
    if a[i] == element:
        position = i
        break
if position > -1:
    print(position)
else:
    print(" -1 Element dies not exist")