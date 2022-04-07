list1 = [1,2,4]
list2 = [1,3,4]
list=[]
i=0
while i<len(list1):
    j=0
    while j<len(list2):
        if i==j:
            list.append(list1[i])
            list.append(list2[j])
        j=j+1
    i=i+1 
print(list)           