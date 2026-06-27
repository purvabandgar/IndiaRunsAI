# Import required libraries
import json
import csv

# Import scoring modules

from score_skills import calculate_skill_score
from score_experience import calculate_experience_score
from score_behavior import calculate_behavior_score
from score_career import calculate_career_score
from score_jd_fit import calculate_jd_fit
from rank_candidates import rank_candidates

# Load Job Description
with open("data/jd.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()

# Store candidate scores
candidates_scores = []

# Read candidate dataset
with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for i, line in enumerate(f):

        # Show processing progress
        if i % 100 == 0:
            print("Processed:", i)

        candidate = json.loads(line)

        # Extract candidate skills
        candidate_skills = [
            skill["name"]
            for skill in candidate["skills"]
        ]

        # Calculate skill score
        skill_score = calculate_skill_score(candidate_skills)

        # Create candidate text for JD matching
        candidate_text = ""

        candidate_text += candidate["profile"]["headline"] + " "
        candidate_text += candidate["profile"]["summary"] + " "

        for job in candidate["career_history"]:
            candidate_text += job["title"] + " "
            candidate_text += job["description"] + " "

        for skill in candidate["skills"]:
            candidate_text += skill["name"] + " "

        # Calculate JD keyword matching score
        jd_fit_score = calculate_jd_fit(candidate_text)

        # Calculate experience score
        experience_score = calculate_experience_score(
            candidate["profile"]["years_of_experience"]
        )

        # Calculate behavioural score
        behavior_score = calculate_behavior_score(
            candidate["redrob_signals"]
        )

        # Calculate career relevance score
        career_score = calculate_career_score(
            candidate["career_history"]
        )

        # Semantic scoring module implemented separately.
        # Disabled in the final pipeline to reduce runtime on 100K candidates.
        semantic_score = 0

        # Calculate final weighted score
        final_score = (
            skill_score * 4
            + experience_score * 2
            + behavior_score
            + career_score
            + jd_fit_score
            + (semantic_score * 100)
        )

        # Store candidate score
        candidates_scores.append({
            "candidate_id": candidate["candidate_id"],
            "final_score": round(final_score, 2)
        })

# Rank candidates
candidates_scores = rank_candidates(candidates_scores)

# Display Top 100 candidates
print("\nTOP 100 CANDIDATES\n")

for candidate in candidates_scores[:100]:
    print(candidate)

# Save ranked candidates
with open("submission.csv", "w", newline="", encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow(["candidate_id", "score"])

    for candidate in candidates_scores[:100]:
        writer.writerow([
            candidate["candidate_id"],
            candidate["final_score"]
        ])

print("\nsubmission.csv created successfully!")

with open("top5_candidates.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(["candidate_id", "score"])

    for candidate in candidates_scores[:5]:
        writer.writerow([
            candidate["candidate_id"],
            candidate["final_score"]
        ])

print("top5_candidates.csv created successfully!")