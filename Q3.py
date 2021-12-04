#Ways to remove a key from dictionary

class Program:
    def Dictionary(self):
        test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}

        new_dict={key:val for key,val in test_dict.items() if key!="Mani"}

        return new_dict

def main():
    obj=Program()
    ret=obj.Dictionary()
    print("after removal: ",ret)

if __name__=="__main__":
    main()


#Another way is by using pop() on dictionary.