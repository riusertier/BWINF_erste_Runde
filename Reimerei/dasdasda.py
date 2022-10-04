import re
last = []
grundword = 'Besuch'
for m in re.finditer('e', grundword):
    last.append(m.start())

try:
    ind = last[-2]
except IndexError:
    ind = last[-1]

ab_maß = grundword[ind:]

print(ab_maß)