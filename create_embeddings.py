import requests
import os
import json
import pandas as pd 

def create_embedding(text_list):
    r = requests.post(
        "http://localhost:11434/api/embed",
        json={
            "model": "bge-m3",
            "input": text_list
        }
    )

    embeddings = r.json()['embeddings']
    return embeddings



jsons = os.listdir("jsons")     # List all files in the "jsons" directory

my_dicts = []
chunk_id = 0

for json_file in jsons:
    with open(f"jsons/{json_file}") as f:
        content = json.load(f)

    if isinstance(content, dict):
        chunks = content.get("chunks", [])                    
    elif isinstance(content, list):
        chunks = content
    else:
        chunks = []

    if not chunks:
        continue

    embeddings = create_embedding([c['text'] for c in chunks])

    for i,chunk in enumerate(chunks):
        chunk['chunk_id'] = chunk_id
        # chunk['embedding'] = create_embedding(chunk['text'])
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        my_dicts.append(chunk)
        print(chunk)
    break                   # for one file only

# print(my_dicts)


df = pd.DataFrame(my_dicts)
print(df)