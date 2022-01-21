import collections

# score[index] -> dict[letter] -> count
score = []
guess_score = {}
guesses = []
solutions = []

def parse():
    data = open("guesses.txt", "r")
    rlines = data.readlines()

    for line in rlines:
        line = line.strip()
        guesses.append(line)

    data = open("solutions.txt", "r")
    rlines = data.readlines()

    for line in rlines:
        line = line.strip()
        solutions.append(line)

def analyze():
    global score

    for i in range(5):
        score.append(collections.defaultdict(int))

    for s in solutions:
        for i in range(len(s)):
            c = s[i]
            score[i][c] += 1

    for g in guesses:
        g_score = 0
        for i in range(len(g)):
            c = g[i]
            g_score += score[i][c]

        guess_score[g] = g_score

def dump():
    sorted_dict = {k: v for k, v in sorted(guess_score.items(), key=lambda item: item[1])}
    data = open("position_score.txt", "w")
    for k,v in reversed(sorted_dict.items()):
        data.write(k + " " + str(v) + '\n')

    data = open("position_score_table.txt", "w")
    for c in "abcdefghijklmnopqrstuvwxyz":
        line = c + " "
        for i in range(5):
            line += str(score[i][c]) + " "
        
        data.write(line + "\n")


def main():
    parse()
    analyze()
    dump()

main()
