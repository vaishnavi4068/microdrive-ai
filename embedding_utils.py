import os
import csv
import numpy as np
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

EMBED_MODEL = "models/embedding-001"
HASHTAG_CSV = "hashtags.csv"

# Helper: embed text
def embed_text(text: str):
    response = genai.embed_content(
        model=EMBED_MODEL,
        content=text
    )
    # Defensive: check embeddings
    if not response['embedding']:
        raise ValueError("No embeddings returned from Gemini API.")
    return np.array(response['embedding'])

# Helper: load hashtags and their embeddings from CSV
# CSV format: hashtag,embedding_json
# Example row: #vegan,"[0.1, 0.2, ...]"
def load_hashtag_embeddings():
    hashtags = []
    embeddings = []
    with open(HASHTAG_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 2:
                continue
            hashtags.append(row[0])
            emb = np.array(eval(row[1]))
            embeddings.append(emb)
    return hashtags, np.stack(embeddings)

# Helper: cosine similarity
def cosine_similarity(a, b):
    a = a / np.linalg.norm(a)
    b = b / np.linalg.norm(b, axis=1, keepdims=True)
    return np.dot(b, a)

# Main function: get top 5 hashtags
def get_top_hashtags(photo_description: str):
    desc_emb = embed_text(photo_description)
    hashtags, hashtag_embs = load_hashtag_embeddings()
    sims = cosine_similarity(desc_emb, hashtag_embs)
    top_idx = np.argsort(sims)[-5:][::-1]
    return [hashtags[i] for i in top_idx] 