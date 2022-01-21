# dumps the top+bottom N empty intersections, which have unique letters
import collections

intersection = dict()
pos_score = dict()
N = 5
result = dict()
interest = dict()

def parse():
    # count solutions
    data = open("solutions.txt", "r")
    rlines = data.readlines()
    count_solutions = len(rlines)

    # count intersections
    data = open("empty_intersection_count.txt", "r")
    rlines = data.readlines()

    for line in rlines:
        line = line.strip()
        s = line.split(" ")
        intersection[s[0]] = count_solutions - int(s[1])

    # position score
    data = open("position_score.txt", "r")
    rlines = data.readlines()

    for line in rlines:
        line = line.strip()
        s = line.split(" ")
        pos_score[s[0]] = int(s[1])

# returns True if s contains a duplicate letter
def dupe(s):
    for i in range(len(s)):
        c = s[i]
        if c in s[i+1:]:
            return True

    return False

# scores word as intersection count + letter position score
def analyze():
    global result

    for k,v in intersection.items():
        result[k] = v + pos_score[k]
    sorted_dict = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}
    result = sorted_dict

    count = 0
    for k,v in reversed(result.items()):
        if dupe(k):
            # skip duplicates
            continue

        interest[k] = v
        
        count += 1
        if count > 2000:
            break

# returns True if the intersection of the characters in strings a and b is non-empty
def intersect(a,b):
    for c in a:
        if c in b:
            return True

    return False

# find two words, with no intersections that have maximum position score
def find_two():
    max_score = 0
    max_words = ()
    for ki,vi in interest.items():
        for kj,vj in interest.items():
            if not intersect(ki, kj):
                score = vi + vj
                if score > max_score:
                    max_words = (ki, kj)
                    print(score, max_words)
                    max_score = score

def dump():
    data = open("position_intersection_score.txt", "w")
    for k,v in reversed(result.items()):
        data.write(k + " " + str(v) + '\n')

def main():
    parse()
    analyze()
    find_two()
    dump()

main()
