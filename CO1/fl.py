s=input(("Enter a string\n"))
x=list(s)
temp=x[0]
x[0]=x[-1]
x[-1]=temp
print("".join(x))
