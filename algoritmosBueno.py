import bbdd
import math



def mediaSentencia(user, pelis):
    sentencia='SELECT avg(rating) from rating WHERE userId ='+str(user)+' and ('
    for i in pelis:
        sentencia+='movieId = '+str(i)+' or '
    sentencia=sentencia[:-3]
    sentencia+=')'
    return sentencia

def prediccion(u,p):
    numerador = 0
    denominador = 0
    votadas = bbdd.votadas(u)
    for i in range(len(votadas)):
        similitud = sim(votadas[i][0],p)
        # TODO: filtro de umbral
        numerador += similitud * votadas[i][1]
        denominador += similitud
    return numerador/denominador

def sim(mid1,mid2):
    ratings1 = bbdd.sameEnery(mid1,mid2)
    ratings2 = bbdd.sameEnery(mid2,mid1)
    numerador=0
    denominador1=0
    denominador2=0
    denominador=0
    # print(ratings1[1])
    # print(ratings1[0][1])
    sentencia='SELECT movieId FROM rating WHERE userId = '+str(ratings1[0][1])+' and userId IN (SELECT userId FROM rating WHERE movieId='+str(mid1)+' AND userId IN (SELECT userId FROM rating WHERE movieId='+str(mid2)+'))'
    for j in ratings1:
        sentencia+='INTERSECT SELECT movieId FROM rating WHERE userId = '+str(j[1])+' and userId IN (SELECT userId FROM rating WHERE movieId='+str(mid1)+' AND userId IN (SELECT userId FROM rating WHERE movieId='+str(mid2)+'))'
    # print(sentencia)
    # bbdd.commonFilms(sentencia)
    # bbdd.media(mediaSentencia(ratings1[0][1],bbdd.commonFilms(sentencia)))
    notaPonderada1 = []
    notaPonderada2 = []

    for i in range(len(ratings1)):
        print('-',i)
        notaPonderada1.append(ratings1[i][0] - bbdd.media(mediaSentencia(ratings1[i][1],bbdd.commonFilms(sentencia))))
        notaPonderada2.append(ratings2[i][0] - bbdd.media(mediaSentencia(ratings2[i][1],bbdd.commonFilms(sentencia))))

        numerador+=notaPonderada1[i]*notaPonderada2[i]
        denominador1+=notaPonderada1[i]**2
        denominador2+=notaPonderada2[i]**2
    denominador=math.sqrt(denominador1)*math.sqrt(denominador2)
    return numerador/denominador

# iid=5
uid = 2
# votadas = bbdd.votadas(uid)
# noVotadas =bbdd.noVotadas(uid) 

for i in bbdd.noVotadas(uid):
    print(prediccion(uid,i))

# sim(1,3)
# print(round(sim(1,),2))
# la 1 y la 14
# la 1 y la 3
# la 1 y la 456
# la 1 y la 6547 pensarla

print(round(prediccion(53,1),2))
# usuario 53
