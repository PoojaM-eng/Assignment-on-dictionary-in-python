#Extract Unique values dictionary values

class Program:
    def Dictionary(self):
        test_dict = {'gfg': [5, 6, 7, 8],
                     'is': [10, 11, 7, 5],
                     'best': [6, 12, 10, 8],
                     'for':[1,2,5]}
        print("The original dictionary is : " + str(test_dict))                 #original dictionary

        res=list(sorted({ele for val in test_dict.values() for ele in val}))

        # printing result
        print("The unique values list is : " + str(res))

def main():
    obj=Program()
    obj.Dictionary()

if __name__=="__main__":
    main()