'''
质数因子
'''

import math


def divide_to_prime(n, p_list):
    if n < 2:
        return
    if n % 2 == 0:
        p_list.append(2)
        divide_to_prime(n // 2, p_list)
    elif n % 3 == 0:
        p_list.append(3)
        divide_to_prime(n // 3, p_list)
    elif n % 5 == 0:
        p_list.append(5)
        divide_to_prime(n // 5, p_list)
    else:
        temp = p_list.copy()
        for i in range(5, int(math.sqrt(n)) + 1, 6):
            if n % i == 0:
                divide_to_prime(i, p_list)
                divide_to_prime(n // i, p_list)
            elif n % (i + 2) == 0:
                divide_to_prime(i + 2, p_list)
                divide_to_prime(n // (i + 2), p_list)
        if len(p_list) == len(temp):
            p_list.append(n)


while True:
    try:
        num = int(input())
        PrimeFactor = []

        divide_to_prime(num, PrimeFactor)

        for x in PrimeFactor:
            print(x, end=' ')
    except:
        break
