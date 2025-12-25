file = open('tem.txt', 'r')
s = []
for i in file:
    i = float(i)
    s.append(i)
print(sum(s))
print(max(s))
print(min(s))
