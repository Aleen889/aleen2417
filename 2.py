m=int(input('enter a number:'))
i=[]
while m>0 :
    i.append(m%2)
    m=m//2
    i.reverse()
for m in i:
    print(m,end=" ")
        
