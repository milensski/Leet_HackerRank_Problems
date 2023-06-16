records = []
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())

    records.append([name, score])
    scores.append(score)

sorted_records = sorted(records, key=lambda x: x[1])
filtered_scores = []
[filtered_scores.append(x) for x in scores if x not in filtered_scores]
filtered_scores.sort()
second_lowest = filtered_scores[1]

names = []

for name, score in sorted_records:
    if score == second_lowest:
        names.append(name)

for name in sorted(names):
    print(name)
