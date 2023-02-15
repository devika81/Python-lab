a={'dev':30,'gok':10,'anu':70,'fathu':11}
l=list(a.items())
l.sort()
print('Ascending order is\n',l)
l=list(a.items())
l.sort(reverse=True)
print('Descending order is\n',l)
dict=dict(l)
print("Dictionary",dict)
