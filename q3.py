import json
n=input("entet your name")
mark=0
v=[]
with open ("al.json","r") as k:
    al=json.loads(k.read())
for i in al :
    resp=input("enter the response:")
    v.append(resp)
    if resp==al[i]:
        print("true answer")
        mark=mark+1
    else:
        print("false answer")
q=(n,v)
print(q)
print("your mark is :",mark)
