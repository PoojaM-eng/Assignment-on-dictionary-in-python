#Append Dictionary Keys and Values ( In order ) in dictionary

from itertools import chain
class Program:

    def Dictionary(self):
        # initializing dictionary
        test_dict = {"Gfg": 1, "is": 3, "Best": 2}

        print("original dictionary is: ",str(test_dict))

        res=list(test_dict.keys())+list(test_dict.values())

        return res
    def Dictionary1(self):
        # initializing dictionary
        test_dict1 = {"Gfg": 1, "is": 3, "Best": 2}

        print("original dictionary is: ",str(test_dict1))
        res=list(chain(test_dict1.keys(),test_dict1.values()))
        return res

def main():
    obj=Program()
    ret=obj.Dictionary()
    ret1=obj.Dictionary1()
    print("dictionary after recreation: ",ret)
    print("dictionary after recreation by using chain: ", ret1)


if __name__=="__main__":
    main()