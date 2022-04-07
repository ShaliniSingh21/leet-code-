a= [2,5,6,0,0,1,2]
element = int(input("Enter Number"))
p=-1
for i in range(len(a)):
    if a[i] == element:
        p=i
if p>-1:       
    print("true")
  
else:
    print("false")  
    #     break  
       