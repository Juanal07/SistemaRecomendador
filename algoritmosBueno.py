import bbdd

uid = 2
votadas = bbdd.votadas(uid)
noVotadas =bbdd.noVotadas(uid) 

def sim(mid1,mid2):
    ratings1 = bbdd.sameEnery(mid1,mid2)
    ratings2 = bbdd.sameEnery(mid2,mid1)
    for i in ratings1:
        media(uid)

def media(uid):

    return 5



for i in votadas:
    for j in noVotadas:
        sim(i,j)
