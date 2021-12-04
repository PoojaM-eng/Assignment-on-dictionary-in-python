def mirrorChar(input,k):
    # create dictionary
    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dictChar=dict(zip(original,reverse))

    # separate out string after length k to change
    # characters in mirror

    prefix=input[0:k-1]
    suffix=input[k-1:]
    mirror=''

    # separate out string after length k to change
    # characters in mirror

    for i in range(0,len(suffix)):
        mirror=mirror+dictChar[suffix[i]]

    print(prefix+mirror)

# Driver program
if __name__ == "__main__":
    input = 'paradox'
    k = 3
    mirrorChar(input,k)