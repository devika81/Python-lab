string=input("Enter the string:\n")
frequency={}
for i in string:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print("The number of characters in the string is",frequency)        
