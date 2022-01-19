import collections

solutions = set()
double_count = 0

def parse():
    data = open("solutions.txt", "r")
    rlines = data.readlines()

    for line in rlines:
        line = line.strip()
        solutions.add(line)


def analyze():
    global double_count
    for s in solutions:
        for i in range(len(s)):
            c = s[i]
            if c in s[i+1:]:
                double_count +=1
                break

    per = 100 * double_count / len(solutions)
    print("double_count", double_count, "solution count", len(solutions), per)

def main():
    parse()
    analyze()

main()
