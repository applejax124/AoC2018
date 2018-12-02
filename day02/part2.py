import sys

boxes = []

for line in sys.stdin:
    line = line.strip()
    boxes.append(line)
    
for a in boxes:
    for b in boxes:
        if a == b: 
            continue

        diffs = 0
        final = []
        for x,y in zip(a,b):
            if x!=y:
                diffs += 1
            if x==y:
                final.append(x)

        if diffs == 1:
            print(''.join(final))
            sys.exit(0)
