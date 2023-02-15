s=input("Enter a string:")
unique=set(s.split())
words=s.split()
count=dict()
for word in unique:
    count[word]=words.count(word)
print(count)
