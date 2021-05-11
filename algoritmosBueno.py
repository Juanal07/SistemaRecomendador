import bbdd
import math

uid = 2
votadas = bbdd.votadas(uid)
noVotadas =bbdd.noVotadas(uid) 

def sim(mid1,mid2):
    ratings1 = bbdd.sameEnery(mid1,mid2)
    ratings2 = bbdd.sameEnery(mid2,mid1)
    numerador=0
    denominador1=0
    denominador2=0
    denominador=0
    for i in ratings1:
        ratings1[i]-=media()
        ratings2[i]-=media()
        numerador+=ratings1[i]*ratings2[i]
        denominador1+=ratings1[i]**2
        denominador2+=ratings2[i]**2
    denominador=math.sqrt(denominador1)+math.sqrt(denominador2)
    return numerador/denominador

def media():

    return 5

prediccion=0

for i in votadas:
    for j in noVotadas:
        sim(i,j)
