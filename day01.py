from day01_input import feed

# 1.1 Find max
print(max(sum(list(map(int, g.strip().split("\n")))) for g in feed.split("\n\n")))

# 1.2 Find top 3
print(sum(sorted(sum(list(map(int, g.strip().split("\n")))) for g in feed.split("\n\n"))[-3:]))
