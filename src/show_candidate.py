import json

candidate_id = "CAND_0081846"
with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        if candidate["candidate_id"] == candidate_id:
            print(candidate)
            break