list=[12,6,2,4,13,63,35,23]
no=int(input("enter the no"))
i=0
while i<len(list):
    if  no in list[i]:
        print(no,list.index)
    else:
        print("no is not in list")    
    i=i+1