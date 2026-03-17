import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib
import requests

def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed",json = {
        "model" : "bge-m3",
        "input" : text_list
    })

    embedding = r.json()['embeddings']
    return embedding

df = joblib.load('embeddings.joblib')


incoming_query = input("Ask a Question about the couerse:")
question_embedding = create_embedding([incoming_query])[0]
# print(question_embedding)

similarities = cosine_similarity(np.vstack(df['embedding']),[question_embedding]).flatten()
print(similarities)
max_index = similarities.argsort()[::-1] [0:3] # top 3 similar chunks
print(max_index)

new_df = df.loc[max_index]
print(new_df[["number","text"]])