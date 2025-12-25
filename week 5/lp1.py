def filter_high_scores(scores, threshold):
    high_s = []
    for score in scores:
        if score >= threshold:
            high_s.append(score)
    return high_s

print(filter_high_scores([88, 91, 75, 99, 82], 90))
print(filter_high_scores([10, 25, 50, 75], 50))
print(filter_high_scores([60, 70, 80], 90))