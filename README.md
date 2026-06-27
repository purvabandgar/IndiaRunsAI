# AI Candidate Ranking System

## Overview

This project was developed for the **India Runs AI Hackathon 2026 – Intelligent Candidate Discovery Challenge**.

The system intelligently ranks candidates by evaluating multiple factors instead of relying only on keyword matching. It combines job description relevance, candidate skills, professional experience, career history, and behavioral signals to generate an accurate ranked candidate list.

---

## Features

* Multi-factor candidate ranking
* Job Description (JD) keyword matching
* Skill-based scoring
* Experience evaluation
* Career history analysis
* Behavioral signal scoring
* Semantic ranking module (implemented)
* Automatic Top 100 candidate selection
* Submission file generation

---

## Project Structure

```text
IndiaRunsAI/
│
├── data/
│   ├── jd.txt
│   ├── candidate_schema.json
│   ├── sample_candidates.json
│   └── sample_submission.csv
│
├── src/
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
├── output/
│   └── submission.csv
│
├── submission.csv
├── top5_candidates.csv
├── requirements.txt
└── README.md
```

---

## Ranking Pipeline

The ranking algorithm evaluates each candidate using:

* JD Fit Score
* Skill Match Score
* Experience Score
* Career History Score
* Behavioral Score

The weighted scores are combined to produce the final ranking score.

---

## Technologies Used

* Python
* Sentence Transformers
* NumPy
* Pandas
* Scikit-learn

---

## Runtime Optimization

The project includes a semantic similarity module using **BAAI/bge-small-en-v1.5**.

To optimize execution time for approximately 100,000 candidate profiles, semantic scoring is implemented but disabled during the final ranking process. This significantly reduces runtime while maintaining efficient multi-factor candidate ranking.

---

## Output

The system automatically generates:

* Top 100 Ranked Candidates
* submission.csv
* top5_candidates.csv

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python src/main.py
```

---

## Author

**Purva Bandgar**

India Runs AI Hackathon 2026
