import sys

c = 0
freqs = []
s = set()

for line in sys.stdin:
    freqs.append(line)
    if line.startswith('+'):
        line = line.split('+')
        c += int(line[1])
    elif line.startswith('-'):
        line = line.split('-')
        c -= int(line[1])
    if c not in s:
        s.add(c)
    else:
        print(c)

while True:
    for f in freqs:
        if f.startswith('+'):
            f = f.split('+')
            c += int(f[1])
        elif f.startswith('-'):
            f = f.split('-')
            c -= int(f[1])
    
        if c not in s:
            s.add(c)
        else:
            print(c)
            sys.exit(0)
