s='олена, микола, наталія, василь'
a=s.split()
s=''
for i in range(len(a)):
    a[i]=a[i].capitalize()
    s+=a[i]+' '
print(s)