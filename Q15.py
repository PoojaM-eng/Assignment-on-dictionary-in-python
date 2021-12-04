#Function to find the size of largest subset
# of anagram words

from collections import Counter

def maxAnagramsize(input):
    # split input string separated by space
    input=input.split(" ")
    # sort each string in given list of strings
    for i in range(0,len(input)):
        input[i]=''.join(sorted(input[i]))

    # now create dictionary using counter method
    # which will have strings as key and their
    # frequencies as value

    freqdict=Counter(input)

    # get maximum value of frequency
    print(max(freqdict.values()))

if __name__ == "__main__":
    input = 'ant magenta magnate tan gnamate'
    maxAnagramsize(input)
