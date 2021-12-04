#Convert a list of Tuples into Dictionary

list1=[("Nakul",93), ("Shivansh",45), ("Samved",65),
           ("Yash",88), ("Vidit",70), ("Pradeep",52)]

dict1=dict()

for student,score in list1:
    dict1.setdefault(student,[]).append(score)

print(dict1)
