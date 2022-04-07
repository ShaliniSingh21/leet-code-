list=[-1,2,5,7,9,3,1]
no=int(input("enter the no"))
i=0
while i<len(list):
    if list[i]==no:
        print("index of no is",list.index(no)," it's exist in this list")
        break
    else:
        print(" not exist") 
        break   
    i=i+1    