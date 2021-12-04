#Remove all duplicates words from a given sentence

from collections import Counter

def remov_duplicates(input):
    # split input string separated by space
    input=input.split(" ")

    # joins two adjacent elements in iterable way
    for i in range(0,len(input)):
        input[i]="".join(input[i])

    Uniqdict=Counter(input)

    s=" ".join(Uniqdict.keys())

    print(s)


# Driver program
if __name__ == "__main__":
    input = 'Python is great and Java is also great'
    remov_duplicates(input)