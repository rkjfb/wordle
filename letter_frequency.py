import collections

solutions = set()
result = collections.defaultdict(int)
result_percent = dict()

def parse():
    data = open("solutions.txt", "r")
    rlines = data.readlines()

    for line in rlines:
        line = line.strip()
        solutions.add(line)


def analyze():
    for s in solutions:
        for c in s:
            result[c] += 1

    base = sum(result.values())
    for k,v in result.items():
        result_percent[k] = round(100 * v / base,2)


def dump():
    sorted_dict = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}
    data = open("letter_frequency.txt", "w")
    for k,v in reversed(sorted_dict.items()):
        data.write(k + " " + str(v) + " " + str(result_percent[k]) + '\n')

def main():
    parse()
    analyze()
    dump()

main()
