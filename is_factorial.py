def is_factorial(num):
    fact = 1
    i = 1

    while  i <= num:
        fact *= i
        if fact == num:
            return True
        if fact > num:
            return False
        i += 1
    return False
