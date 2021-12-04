#Merging two Dictionaries

def Merge(dict1,dict2):
    return (dict2.update(dict1))

def Merge1(dict1,dict2):
    res={**dict1,**dict2}
    return res

# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3=Merge1(dict1,dict2)


print(Merge(dict1,dict2))
print(dict3)
print(dict2)
print(dict1)





