import sys

lines = sys.stdin.read().splitlines()[1:]
print(sum(sum(map(int, line.split())) >= 2 for line in lines))