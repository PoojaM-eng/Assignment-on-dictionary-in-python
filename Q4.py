#Ways to sort list of dictionaries by values in Python – Using itemgetter

from operator import itemgetter

lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

print("The list printed sorting by age: ")
print(sorted(lis,key=itemgetter('age')))

print("\r")

# using sorted and itemgetter to print list sorted by both age and name
# notice that "Manjeet" now comes before "Nandini"

print("The list printed sorting by age and name: ")
print(sorted(lis,key=itemgetter('age','name')))

print("\r")

# using sorted and itemgetter to print list sorted by age in descending order
print ("The list printed sorting by age in descending order: ")
print (sorted(lis, key=itemgetter('age'),reverse = True))