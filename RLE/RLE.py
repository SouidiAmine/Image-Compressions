


def compression(chaine):
    result = '' #result finale
    i=0   #indice
    s=1   #nombre de reprtetion
    t=True #si la chaine et deja connue
    while(i<len(chaine)-1):
        if chaine[i]==chaine[i+1]:
            i+=1
            s+=1 #incrementer le nombre de repetition
        else:
            if s > 2: #si une valeur se répète 3 fois ou plus
                result = result +str(s)+chaine[i]

                i += 1
                s = 1
                t = True
            else:
                if t == True :
                    result = result+str(0)+chaine[i-s+1:i+1]
                    i+=1
                    s=1
                    t=False
                if t== False:
                    result = result + chaine[i-s+1:i+1]
                    i+=1
                    s=1

    if s> 2 :result = result +str(s)+chaine[i] #pour la dernier chaine
    else: result = result +chaine[i-s+1:i+1]
    return  result



def compare(chaine,result):
    print()
    return (len(result)/len(chaine))*100


chaine = input('Please Enter your chaine : ')
print('the compress chain: '+compression(chaine))
print ('the compression ratio: '+ str(int (compare(chaine,compression(chaine))))+' %')


