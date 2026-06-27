def calculate_behavior_score(signals):
    score = 0

    score += signals["github_activity_score"]

    score += signals["profile_completeness_score"] / 10

    score += signals["interview_completion_rate"] * 10

    score += signals["recruiter_response_rate"] * 10

    score += signals["saved_by_recruiters_30d"]

    return round(score, 2)