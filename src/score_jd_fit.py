def calculate_jd_fit(candidate_text):

    score = 0

    keywords = [
        "ranking",
        "retrieval",
        "semantic search",
        "recommendation",
        "embeddings",
        "vector",
        "pinecone",
        "qdrant",
        "weaviate",
        "faiss",
        "elasticsearch",
        "opensearch",
        "ndcg",
        "mrr",
        "learning-to-rank",
        "reranking",
        "hybrid retrieval"
    ]

    text = candidate_text.lower()

    for keyword in keywords:
        if keyword in text:
            score += 10

    return score