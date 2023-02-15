print("Genertaion of positive number from the given list:\n")
s=[x for x in[-2,-1,0,5,8,9,-6,-3]if x>0]
print("Positive numbers are:",s)
print("\n")
print("Square of N numbers:\n")
s=[x**2 for x in range(10)]
print("Square of numbers in the list is:",s)
print("\n")
print("Formation of vowels:\n")
l=["owl","cat","umbrella","adventure","ball","eat"]
print("All words are:",l)
for i in l:
 v={x for x in i if x in 'aeiou'}
 print(v,i)
print("\n")        
n=input("Enter a string:")
z=[ord(i) for i in n]
print("The ordinal value of the word",n,"is",z)      
                                                                    
