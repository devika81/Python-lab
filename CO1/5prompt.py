l=[]
n=4
print("Enter numbers")
for i in range(n):
    num=int(input("Num"))
    l.append(num)
print(l)
for i in range(len(l)):
        if(l[i]>100):
            l[i]="over"
print(l)
    
