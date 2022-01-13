import collections

solutions = set()

def parse():
    data = open("solutions.txt", "r")
    rlines = data.readlines()

    for line in rlines:
        line = line.strip()
        solutions.add(line)


def analyze():
    doubles = False
    for s in solutions:
        for i in range(len(s)):
            c = s[i]
            if c in s[i+1:]:
                print("found: " + s)
                doubles = True
                break
        if doubles:
            break

    if not doubles:
        print("no doubles")

def main():
    parse()
    analyze()

main()
