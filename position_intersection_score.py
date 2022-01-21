# dumps the top+bottom N empty intersections, which have unique letters
import collections

intersection = dict()
pos_score = dict()
N = 5
result = dict()

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

def analyze():
    for k,v in intersection.items():
        result[k] = v + pos_score[k]

def dump():
    sorted_dict = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}
    data = open("position_intersection_score.txt", "w")
    for k,v in reversed(sorted_dict.items()):
        data.write(k + " " + str(v) + '\n')

def main():
    parse()
    analyze()
    dump()

main()
