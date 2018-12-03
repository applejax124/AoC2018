import sys

fabric = [['.']*1000 for _ in range(1000)]

for line in sys.stdin:
    line = line.split()

    n = int(line[0].split('#')[1])

    line[2] = line[2].strip(':')
    left, top = map(int, line[2].split(','))

    line[3] = line[3].strip()
    width, height = map(int, line[3].split('x'))

    for h in range(top, top+height):
        for w in range(left, left+width):
            if fabric[h][w] == str(n):
                pass
            elif fabric[h][w] == '.':
                fabric[h][w] = str(n)
            else:
                fabric[h][w] = 'X'

count = 0
for row in fabric: 
    for item in row:
        if item == 'X':
            count += 1
print(count)
