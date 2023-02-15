list1=[1,2,3,4,5,]
list2=[5,6,7,8,9,10]
if(len(list1)==len(list2)):
    print("The lists are of same lengrth\n")
else:
    print("The lists are of different length\n")
print("THe length of the list1 is:",len(list1),
      "the length of list2 is:",len(list2))
if(sum(list1)==(sum(list2))):
   print("\nSum is same\n")
else:
   print("\nSum is different\n")
print("Sum of list1 is:",sum(list1),"Sum of list2 is:",sum(list2))
set1=set(list1)
set2=set(list2)
setin=set1.intersection(set2)
if(setin!=0):
  print("Both set have common values\n")
else:
  print("Both set have different values\n")
print("The value that occur in both is:",setin)
