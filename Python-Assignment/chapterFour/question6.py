def average(first, *second):
    total = first + sum(second)
    count = 1 + len(second)
    return total / count
