from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from utils.embedding import get_embedding

def rank_resumes(job_emb, resumes, top_k=10):
    results = []
    for name, content in resumes:
        emb = get_embedding(content)
        score = cosine_similarity([job_emb], [emb])[0][0]
        results.append((name, score, content))
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:top_k]
