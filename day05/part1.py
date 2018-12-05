import sys

polymer = sys.stdin.readline().strip()
polymer = [p for p in polymer]

changed = True

print(len(polymer))

while changed:
    changed = False
    for i in range(len(polymer)-1):
        left = polymer[i]
        right = polymer[i+1]

        if (left.isupper() and right.islower()) or (left.islower() and right.isupper()):
            left = left.lower()
            right = right.lower()
            if left == right:
                polymer[i] = "-"
                polymer[i+1] = "-"
                changed = True

    for p in polymer:
        if p == '-':
            polymer.remove(p)
        
print(len(polymer))
