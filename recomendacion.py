from textblob import TextBlob
from bson.objectid import ObjectId
from flask import Flask, request
from pymongo import MongoClient
import requests
import numpy as np
import seaborn as sns
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as distance

client = MongoClient("mongodb://localhost:27017/Emotion")
db = client.get_database()

collection1 = db.Message
data1 = pd.DataFrame(list(collection1.find()))
affinity = data1[['user', 'message']]
agrupado = affinity.groupby('user').agg(lambda col: ', '.join(col))
convers = agrupado.reset_index()
toDict = convers.set_index('user').to_dict('dict')
for clave, valor in toDict.items():
    elementos = ", ".join(valor.values())
a = valor
count_vectorizer = CountVectorizer()
sparse_matrix = count_vectorizer.fit_transform(valor.values())
doc_term_matrix = sparse_matrix.todense()
df = pd.DataFrame(doc_term_matrix,
                  columns=count_vectorizer.get_feature_names(),
                  index=a.keys())
similarity_matrix = distance(df, df)
sim_df = pd.DataFrame(similarity_matrix, columns=a.keys(), index=a.keys())
np.fill_diagonal(sim_df.values, 0)


def cadaUsuario(user_id):
    a = sim_df[ObjectId(user_id)]
    a = pd.DataFrame(a)
    similares = a.sort_values([ObjectId(user_id)], ascending=False).head(3)
    similares = similares.reset_index().rename(columns={'index': 'Usuarios'})
    a = list(similares.Usuarios)
    return getname(a)


def getname(numerito):
    recomendados = []
    for i in numerito:
        query = {'_id': ObjectId(i)}
        coll_user = db['User']
        nombre = list(coll_user.find(query, {'_id': 0, 'user': 1}))
        recomendados.append(nombre)
    return recomendados
