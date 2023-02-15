s=input("Enter the strings separated by space:\n")
l=s.split()
print(l)
n=len(l[0])
x=l[0]
for i in l:
    if len(i)>n:
        x=i
print("The longest word is",x)        
