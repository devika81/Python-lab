num=int(input("Enter the number whose factors are to be found:"))
for i in range(1,num+1):
    if num%i==0:
        print(i)
