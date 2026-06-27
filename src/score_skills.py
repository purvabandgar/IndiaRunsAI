JD_SKILLS = [
    "Fine-tuning LLMs",
    "LoRA",
    "Milvus",
    "Python",
    "Embeddings",
    "Retrieval",
    "Ranking"
]

def calculate_skill_score(candidate_skills):
    matches = 0

    for skill in candidate_skills:
        if skill in JD_SKILLS:
            matches += 1

    return matches