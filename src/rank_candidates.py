def rank_candidates(candidates):
    """
    Sort candidates by final_score in descending order.
    """
    ranked = sorted(
        candidates,
        key=lambda x: x["final_score"],
        reverse=True
    )
    return ranked