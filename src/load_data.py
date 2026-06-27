import json
from pprint import pprint

target = "CAND_0039754"

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:

        candidate = json.loads(line)

        if candidate["candidate_id"] == target:

            print("\nPROFILE\n")
            pprint(candidate["profile"])

            print("\nCAREER HISTORY\n")
            pprint(candidate["career_history"])

            print("\nSKILLS\n")
            pprint(candidate["skills"])

            break