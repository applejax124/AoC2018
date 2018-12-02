import sys

twos = 0
threes = 0

for line in sys.stdin:
    two = False
    three = False
    s = {}
    for l in line:
        if l not in s:
            s[l] = 0
        s[l] += 1
    for l in s:
        if s[l] == 2:
            two = True
        if s[l] == 3:
            three = True

    if two:
        twos += 1
    if three:
        threes += 1

checksum = twos * threes
print(checksum)
