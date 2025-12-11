li=eval(input())          
d={}
for i in range(1,10):
    c=0
    for j in li:
        if j%i ==0:
            c+=1
    d[i]=c
print(d)
