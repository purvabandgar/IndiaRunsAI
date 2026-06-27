from sentence_transformers import SentenceTransformer
from sentence_transformers import util

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

def calculate_semantic_score(jd_text, candidate_text):

    jd_embedding = model.encode(
        jd_text,
        convert_to_tensor=True
    )

    candidate_embedding = model.encode(
        candidate_text,
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        jd_embedding,
        candidate_embedding
    )

    return float(similarity[0][0])