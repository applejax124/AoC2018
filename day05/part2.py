import sys

def react(polymer):
    
    new = [p for p in polymer]
    edited = [n for n in new]

    changed = True

    while changed:

        new = [e for e in edited]
        changed = False

        for i in range(len(new)-1):
            left = new[i]
            right = new[i+1]
    
            if (left.isupper() and right.islower()) or (left.islower() and right.isupper()):
                left = left.lower()
                right = right.lower()
                if left == right:
                    new[i] = "-"
                    new[i+1] = "-"
                    changed = True

        edited = [n for n in new if n != '-']

    return new
    
def remove_letter(letter, polymer):

    new = [p for p in polymer if p.lower() != letter]

    return new

def main():

    lengths = {}

    polymer = sys.stdin.readline().strip()
    polymer = [p for p in polymer]

    polymer = react(polymer)
    print(len(polymer))

    letters = 'abcdefghijklmnopqrstuvwxyz'

    for letter in letters:
        lengths[letter] = len(react(remove_letter(letter, polymer)))

    print(lengths)

if __name__ == "__main__":
    main()
