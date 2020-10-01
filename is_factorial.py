num = int(input("enter the value of num"))
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

res = is_factorial()
print(res)   
