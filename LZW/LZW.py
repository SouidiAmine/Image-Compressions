
dictionary ={}
dic_size= 256

"""he init function below allows to initialize the dictionary with the characters of the ascii
 table from 0 to 255 and initialized to an empty string beyond the 256th character"""
def init():
    global dictionary,dic_size

    dictionary = dict((chr(i), i) for i in range(dic_size))
    dictionary[""] = 256
    dic_size += 1

    return dictionary
"""The search function below takes a character string as input
and returns the value of the string in the dictionary if it exists otherwise returns -1"""
def search(chaine):
    global dictionary, dic_size
    for cle in dictionary.keys() :
        if (cle == chaine):
            return dictionary[cle]

    return -1
"""La fonction insert permettre d’insérer une chaine dans le dictionnaire"""
def insert(chaine):
    global dictionary, dic_size
    dictionary[chaine] = dic_size
    dic_size += 1
    return 0
"""The compress function takes a character string as input and applies LZW compression to it and returns the code of the string"""
def compress(uncompressed):
    global dictionary, dic_size
    w = uncompressed[0]
    result = []
    j = 0
    while (j < len(uncompressed) - 1):
        c = uncompressed[j + 1]

        wc = w + c
        if wc in dictionary:
            w = wc

        else:

            result.append(dictionary[w])
            # Add wc to the dictionary.
            insert( wc)

            w = c
        j += 1

    # write the code of
    #
    # w.
    if w:
        result.append(dictionary[w])
    return result
dictionary = init()
ch = input("Enter your chain :")
print(compress(ch))
print ("dictionary display : ")
print(dictionary)

