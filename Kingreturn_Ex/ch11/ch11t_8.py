def pi(i):
    sum = 0
    for num in range(1, i + 1):
        sum += 4 * ((-1) ** (num + 1) / (2 * num - 1))
    return sum


for tag in range(1, 9002, 1000):
    print("tag = %d, pi(tag) = %f" % (tag, pi(tag)))
