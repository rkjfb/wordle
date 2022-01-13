# dumps the top+bottom N empty intersections, which have unique letters
import collections

empty = dict()
N = 5
result = dict()

def parse():
    data = open("empty_intersection_count.txt", "r")
    rlines = data.readlines()

    for line in rlines:
        line = line.strip()
        s = line.split(" ")
        empty[s[0]] = int(s[1])

# return True if s contains a double (or more) character
def double(s):
    for i in range(len(s)):
        c = s[i]
        if c in s[i+1:]:
            return True
            print("found: " + s)
    return False

def analyze(it):
    count = 0
    for k,v in it:
        if double(k):
            continue
        result[k] = v
        count += 1
        if count >= N:
            return

def dump():
    sorted_dict = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}
    data = open("unique_empty_minmax.txt", "w")
    for k,v in reversed(sorted_dict.items()):
        data.write(k + " " + str(v) + '\n')

def main():
    parse()
    analyze(empty.items())
    analyze(reversed(empty.items()))
    dump()

main()
