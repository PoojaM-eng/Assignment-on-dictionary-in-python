#Insertion at the beginning in OrderedDict

from collections import OrderedDict

inordered_dict=OrderedDict([('akshat',1),('nikhil',2)])

inordered_dict.update({'mani':'3'})

inordered_dict.move_to_end('mani',last=False)

print("resultant dictionary: "+str(inordered_dict))


