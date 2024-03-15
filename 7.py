s="максимальне і мінімальне значення"
a='мальне'
res=0
x=0
for i in range(len(s)):
   b=s[x:i]
   if(a in b):
      x=i+1
      res+=1 

print(res)