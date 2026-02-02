def decision_confidence(lift, pval, segment_variance, sample_size):
    score = 0
    if lift > 0.02:
        score += 30
    elif lift > 0:
        score += 15
    if pval < 0.05:
        score += 30
    elif pval < 0.1:
        score += 15
    if segment_variance < 0.02:
        score += 20
    if sample_size > 1000:
        score += 20
    elif sample_size > 500:
        score += 10
    return score
