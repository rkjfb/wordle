import collections

solutions = set()
result = collections.defaultdict(int)
result_percent = dict()
word_score = dict()

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

    #base = sum(result.values())
    base = len(solutions)
    for k,v in result.items():
        result_percent[k] = round(100 * v / base,2)

# returns True if s contains a duplicate letter
def dupe(s):
    for i in range(len(s)):
        c = s[i]
        if c in s[i+1:]:
            return True

    return False

def score_words():
    global word_score
    for s in solutions:
        if dupe(s):
            continue

        score = 0
        for c in s:
            score += result[c]
        word_score[s] = score

def dump():
    sorted_dict = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}
    data = open("letter_frequency.txt", "w")
    for k,v in reversed(sorted_dict.items()):
        data.write(k + " " + str(v) + " " + str(result_percent[k]) + '\n')

def dump_words():
    sorted_dict = {k: v for k, v in sorted(word_score.items(), key=lambda item: item[1])}
    data = open("freq_word_score.txt", "w")
    for k,v in reversed(sorted_dict.items()):
        data.write(k + " " + str(v) + '\n')

def main():
    parse()
    analyze()
    score_words()
    dump()
    dump_words()


main()
