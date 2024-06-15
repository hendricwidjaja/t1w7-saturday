def add(*args):
    sum = 0
    for each in args:
        sum += each
    return sum

def subtract(*args):
    difference = args[0]
    for each in args[1:]:
        difference = difference - each
    return difference
