a=input("enter your list numbers as 4,12,10,\n")
b= a.split(",")
c=[]
for k in b:
    c.append(int(k))
x=0
y=1
z=2
v=1
while z < len(c):
    if c[x] + c[y] == c[z]:
        print(f"{c[x]}+{c[y]}={c[z]} ....sequence OK ")
    elif c[x] + c[y] != c[z]:
        print(f"{c[x]}+{c[y]} !={c[z]} ....No sequence ")
        v = 0
    x +=1
    y +=1
    z +=1
if v == 0:
    print("Your list is NOT in sequence")
else:
    print("Your list is in sequence")