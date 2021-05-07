import pandas as pd
from surprise import Dataset
from surprise import Reader
from surprise import KNNWithMeans, KNNBasic
# from load_data import data
# from recommender import algo

from collections import defaultdict

def get_top_n(predictions, n=10):
    """Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    """

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

def filtrado():

    # ratings_dict = {
    #     "item": [1, 2, 1, 2, 1, 2, 1, 2, 1],
    #     "user": ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E'],
    #     "rating": [1, 2, 2, 4, 2.5, 4, 4.5, 5, 3],
    # }
    # df = pd.DataFrame(ratings_dict)
    # reader = Reader(rating_scale=(1, 5))
    # data = Dataset.load_from_df(df[["user", "item", "rating"]], reader)
    # print(ratings_dict)

    data = Dataset.load_builtin('ml-100k')
    
    sim_options = {
        "name": "pearson", # Similitud de coseno ajustado
        "user_based": False,  # Basado en items
    }

    algo = KNNBasic(sim_options=sim_options)

    trainingSet = data.build_full_trainset()
    algo.fit(trainingSet)
    print('Hasta aqui entrenamiento')

    vecinos_peli = algo.get_neighbors(333, k=3)
    print(vecinos_peli)
    
    # print('Empieza la prediccion')
    # testset = trainingSet.build_anti_testset()
    # predictions = algo.test(testset)
    # print('Hasta aqui la prediccion')
    # for x in range(0,len(predictions)):
    #     uid = predictions[x].uid
    #     iid = predictions[x].iid
    #     est = predictions[x].est
    #     print('[',x,']','User: ',uid, 'Pelicula: ',iid,'Nota: ',round(est, 2))

    # top_n = get_top_n(predictions, n=3)
    # print(top_n)
    # # TODO: motrar nombre de pelicula+iid

