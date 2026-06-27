# AI Candidate Ranking System

## Overview

This project is developed for the India Runs AI Hackathon – Track 1.

The system intelligently ranks candidates by analyzing multiple signals instead of relying only on keyword matching. It evaluates candidate profiles using job description relevance, skills, experience, career history, and behavioral signals to generate a reliable ranked shortlist.

---

## Features

* Multi-factor candidate ranking
* Job Description keyword matching
* Skill-based scoring
* Experience evaluation
* Career history analysis
* Behavioral signal scoring
* Semantic ranking module (implemented)
* Automatic Top 100 candidate selection
* Submission file generation

---

## Project Structure

```
IndiaRunsAI/

│── data/
│   ├── jd.txt
│   └── candidates.jsonl
│
│── src/
│   ├── main.py
│   ├── load_data.py
│   ├── score_skills.py
│   ├── score_experience.py
│   ├── score_behavior.py
│   ├── score_career.py
│   ├── score_jd_fit.py
│   ├── score_semantic.py
│   ├── rank_candidates.py
│   └── show_candidate.py
│
├── requirements.txt
├── submission.csv
└── README.md
```

---

## Ranking Pipeline

The ranking system evaluates candidates using:

* JD Fit Score
* Skill Match Score
* Experience Score
* Career Score
* Behavioral Score

Each score contributes to a weighted final ranking score.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Sentence Transformers
* Scikit-learn

---

## Runtime Optimization

A semantic similarity module using **BAAI/bge-small-en-v1.5** was implemented.

For full dataset execution (~100K candidates), semantic scoring was disabled in the final ranking pipeline to reduce runtime while maintaining efficient multi-factor candidate ranking.

---

## Output

The system automatically generates:

* Ranked Top 100 Candidates
* submission.csv

---

## How to Run

Install dependencies

```
pip install -r requirements.txt
```

Run

```
python src/main.py
```

---

## Author

Purva Bandgar
India Runs AI Hackathon 2026
