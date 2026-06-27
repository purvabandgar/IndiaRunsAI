def calculate_experience_score(years):

    if 5 <= years <= 9:
        return 15

    elif 4 <= years < 5:
        return 10

    elif 9 < years <= 12:
        return 8

    elif 12 < years <= 15:
        return 5

    else:
        return 2