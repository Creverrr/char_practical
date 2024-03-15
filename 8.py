s="Класичні алгоритми опрацювання двовимірних масивів"
a="двовимірних"
b="одновимірних"
j=0
x=0
y=0
for i in range(len(s)):
    if(s[i]==a[j] and j==0):
        j+=1
        x=i
    elif s[i]==a[j] and j==6:
        y=i
        j=0
        break
    elif s[i]==a[j]:
        j+=1
    else:
        x=0
        y=0
        j=0
s=s[:x]
s=s+b+" масивів"
print(s)