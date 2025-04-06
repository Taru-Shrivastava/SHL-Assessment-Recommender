from flask import Flask, request, render_template, jsonify
import ollama, numpy as np, pickle, json
from scrape_jd import scrape_text_from_url

app = Flask(__name__)
with open("faiss_index.pkl", "rb") as f:
    index, shl_data = pickle.load(f)

def get_embedding(text):
    return np.array(ollama.embeddings(model="nomic-embed-text", prompt=text)["embedding"])

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    query = data.get("query", "")
    is_url = data.get("is_url", False)

    if is_url:
        query = scrape_text_from_url(query)

    if not query:
        return jsonify([])

    vec = get_embedding(query).reshape(1, -1)
    _, I = index.search(vec, 10)
    results = [shl_data[i] for i in I[0]]
    return jsonify(results)