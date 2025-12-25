score1 = 85
score2 = 92 
score3 = 78
scores = [score1, score2, score3]
highest = max(score1, score2, score3)
lowest = min(score1, score2, score3)
average = sum(score3, score1, score3)/len(score3, score1, score3)
decim = round(average, 2)
difference = abs(max(score1, score2, score3) - min(score1, score2, score3))
for i in range(scores):
    print(pow(i, 2))

print(highest)
print(lowest)
