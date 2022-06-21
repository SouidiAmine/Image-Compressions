
import cv2
import numpy as np
import matplotlib.pyplot as plt


def quantifier(list , x,y):
    listquantifier = []
    listvalue = np.fromfunction(lambda i, j : 1+(1+i+j) *6, (8,8) , dtype =int)
    t=0
    print(list[0][0:8, 0:8] )
    for i in range(0, x, 8):
        for j in range(0, y, 8):
            listquantifier.append(((list[t][0:8, 0:8] / listvalue).astype(int)).astype(float))

            t = t + 1
    print()
    print(listquantifier[0]*listvalue)
    return listquantifier
def reconstruir(list,x,y):
    listf = []
    t=0
    listvalue = np.fromfunction(lambda i, j: 1 + (1 + i + j) * 6, (8, 8), dtype=int)
    for i in range(0, x, 8):
        for j in range(0, y, 8):
            listf.append((list[t][0:8, 0:8] * listvalue))

            t = t + 1
    return listf
def idctList(list,x,y):
    listf = []
    t=0
    for i in range(0,x, 8):
        for j in range(0, y ,8):
            listf.append(
                cv2.idct(list[t])
            )
            t = t + 1
    return listf

def convertListToImage(list, x,y):
    imgf = np.zeros(shape=(x, y), dtype=np.uint8)
    t=0
    for i in range(0, x, 8):
        for j in range(0, y, 8):
            imgf[i:i + 8, j:j + 8] = list[t][0:8, 0:8]
            t = t + 1

    imgf = np.uint8(imgf)
    return imgf


def diviserImageAvecDCT(image, x,y):
    listem = []
    for i in range(0, x ,8):
        for j in range(0, y, 8):
            listem.append(
                cv2.dct(image[i:i + 8, j:j + 8].astype('float'))
            )
    return listem

img = cv2.imread('lenna.png',0)
#cv2.imshow('Original',img)
img32 = img.astype('float')


l = img32.shape[0]
c = img32.shape[1]

lignes = int(l / 8)
colonnes = int(c / 8)
k1 = (8-l%8)%8 # k c'est le reste des ligne/column qui on va remplir par 0
k2 = (8-c%8)%8





xm = np.pad(img,((0,k1),(0,k2)),'constant')
#print(xm)
listem = diviserImageAvecDCT(xm, l+k1,c+k2)


listemIn = idctList(listem,l+k1,c+k2)





imgf = convertListToImage(listemIn,l+k1,c+k2)
cv2.imshow('Final block ',imgf)
#listem c la list contient les block 8*8 qui on'a s'appliquait a eux la DCT
listQuentifier = quantifier(listem , l+k1,c+k2)
ListFianl = reconstruir(listQuentifier,l+k1,c+k2)
#appliquer la DCT inverse pour chaque block
ListFianl = idctList(ListFianl,l+k1,c+k2)
#conevertir list to image pour le afficher
imageDecompreser = convertListToImage(ListFianl,l+k1,c+k2)

cv2.imshow('Final Decompreser ',imageDecompreser)


cv2.waitKey(0)






































"""
dcti = cv2.idct(imgf.astype('float'))
dcti = dcti.astype('uint8')
plt.imshow(dcti)
plt.show()
cv2.imshow('listem ',listem[0])
listemin = cv2.idct(listem)
listemin = np.uint8(listemin)
cv2.imshow('DCT Inverse ',imgDCTin)
print(listem[0][1,1])
#plt.imshow(listem[0])
plt.show()

   #print("{0} {1}".format(i,j))
#print(listem[0])




for i in range(0,l+k1,8):
    for j in range(0,c+k2,8):
        listem.append(
            cv2.dct(xm[i:i+8,j:j+8].astype('float'))
        )

t =0
imgf = np.zeros(shape=(img.shape[0]+k1,img.shape[1]+k2),dtype=np.uint8)
for i in range(0,l+k1,8):
    for j in range(0,c+k2,8):
        imgf[i:i+8,j:j+8] =listemIn[t][0:8,0:8]
        t=t+1


imgf = np.uint8(imgf)








t=0
for i in range(0,l+k1,8):
    for j in range(0,c+k2,8):
        listemIn.append(
            cv2.idct(listem[t])
        )
        t=t+1
"""