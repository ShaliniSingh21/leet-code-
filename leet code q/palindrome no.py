# palindrome or not                                                                                                                                              s=input("enter")
# a=s.split()      
# i=0
# while i<len(a):
#     i+=1
# k=a[ ::-1]
# if s==k:
#     print("it is palindrome")
    
    
# s=input("enter")
# a=s.split()      
# i=0
# while i<len(a):
#     i+=1
# k=a[ ::-1]
# if s==k:
#     print("it is palindrome")    
# else:
#     print("it is not a palindrome no")    


n=int(input("Enter number:"))
temp=n 
rev=0
while(n>0): 
    dig=n%10 
    rev=rev*10+dig 
    n=n//10 
if(temp==rev): 
    print("The number is a palindrome!") 
else: 
    print("The number isn't a palindrome!") 