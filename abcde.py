a = "[{'id':1,'name':'ajay'}, {'id':2,'name':'akash'}]"
a = a.strip('[]')
a = a.split(', ')
print(a)
print(type(a))
print(a[0])
print(type(a[0]))
