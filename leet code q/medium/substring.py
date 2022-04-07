# s = "abcabcbb"
# i=0
# l=[]
# while i<len(s):
#     if s not in l:
#         l.append(s[i])
       
#     i=i+1 
# print(l)       
 

def Sub_string(s):
    i =0
    j = 0
    d={}
    ans = 0
    while j < len(s):
        if s[j] not in d or i>d[s[j]]:
            ans = max(ans,(j-i+1))
            d[s[j]] = j
        else:
            i = d[s[j]]+1
            ans = max(ans,(j-i+1))
            j-=1
        print(ans)
        j+=1
    return ans
print(Sub_string("ABCABCBB"))        