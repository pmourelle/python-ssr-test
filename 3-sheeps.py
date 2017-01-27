
def sleeping_sheep(num):
    digits = [False] * 10  # each index represents digit presence
    current = num  # value to start with
    iteration = 1  # current number of iteration and multiplier

    while iteration < 100:
        # print('iteration #{}'.format(iteration))
        for v in [int(i) for i in str(current)]:
            # mark digits we got
            digits[v] = True

        if False not in digits:
            # we got them all
            return current

        # next iteration loop values
        iteration = iteration + 1
        current = iteration * num

    if iteration == 100:
        # loop ended out of limit
        return 'INSOMNIA!'


if __name__ == "__main__":
    print('Case #1: 0 --> {}'.format(sleeping_sheep(0)))
    print('Case #2: 1 --> {}'.format(sleeping_sheep(1)))
    print('Case #3: 2 --> {}'.format(sleeping_sheep(2)))
    print('Case #4: 5 --> {}'.format(sleeping_sheep(5)))
    print('Case #5: 11 --> {}'.format(sleeping_sheep(11)))
    print('Case #6: 1692 --> {}'.format(sleeping_sheep(1692)))
