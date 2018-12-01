import sys

c = 0

for line in sys.stdin:
    if line.startswith('+'):
        line = line.split('+')
        c += int(line[1])
    elif line.startswith('-'):
        line = line.split('-')
        c -= int(line[1])

print(c)
