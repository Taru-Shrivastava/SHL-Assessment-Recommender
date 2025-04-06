import json, faiss, numpy as np, ollama, pickle

with open("shl_data.json") as f:
    data = json.load(f)

def get_embedding(text):
    return ollama.embeddings(model="nomic-embed-text", prompt=text)["embedding"]

embeddings = [get_embedding(d["description"]) for d in data]
index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings))

with open("faiss_index.pkl", "wb") as f:
    pickle.dump((index, data), f)