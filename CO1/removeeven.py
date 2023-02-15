list=[10,25,32,47,55]
print(list)
for i in list:
    if(i%2==0):
        list.remove(i)
print("list after removing even numbers:")
print(list)
        
