career_keywords = [
    "ranking",
    "retrieval",
    "recommendation",
    "search",
    "embeddings",
    "vector"
]

def calculate_career_score(career_history):

    score = 0

    for job in career_history:

        description = job["description"].lower()

        for keyword in career_keywords:

            if keyword in description:
                score += 5

    return score