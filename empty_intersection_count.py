guesses = set()
solutions = set()
result = dict()

def parse():
    data = open("guesses.txt", "r")
    rlines = data.readlines()

    for line in rlines:
        line = line.strip()
        guesses.add(line)

    data = open("solutions.txt", "r")
    rlines = data.readlines()

    for line in rlines:
        line = line.strip()
        solutions.add(line)

# returns True if the intersection of the characters in strings a and b is non-empty
def intersect(a,b):
    for c in a:
        if c in b:
            return True

    return False

def analyze():
    for g in guesses:
        empty = 0
        for s in solutions:
            if not intersect(g, s):
                empty += 1
        result[g] = empty

def dump():
    sorted_dict = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}
    data = open("empty_intersection_count.txt", "w")
    for k,v in reversed(sorted_dict.items()):
        data.write(k + " " + str(v) + '\n')

def main():
    parse()
    analyze()
    dump()

main()
