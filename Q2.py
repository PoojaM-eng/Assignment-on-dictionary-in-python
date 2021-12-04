#Python program to find the sum of all items in a dictionary

class Program:
    def Dictionary(self,dict):
        self.sum=0
       # dict={'a': 100, 'b':200, 'c':300}
        for i in dict:
            self.sum+=dict[i]
        return self.sum

def main():
    dict = {'a': 100, 'b': 200, 'c': 300}
    obj=Program()
    ret=obj.Dictionary(dict)
    print("sum of dict values are: ",ret)

if __name__=="__main__":
    main()



