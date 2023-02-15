string=input("Enter a string ending with ing or ly:\n")
if string[-3:]=="ing":
    string+="ly"
else:
    string+="ing"
print(string)    
