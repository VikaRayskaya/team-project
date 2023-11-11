"""
Пользователь вводит 2 целых числа через пробел. Найдите и выведите НОД и НОК двух чисел.
"""

# give name function
def gcd(a, b):#The greatest common divisor
    a = abs(a)
    b = abs(b)
    c = min(a, b)

    gcd_val = 0

    for i in range(c, 0, -1):
        if a % i == 0 and b % i == 0:
            gcd_val = i
            break

    return gcd_val


def lcm(a, b):  #The smallest common multiple
    return a * b / gcd(a, b)


a = int(input())
b = int(input())

if a < 0:
    a = -a

if b < 0:
    b = -b

if a == 0 or b == 0:
    print("НОK = {}".format(min(a, b)))
    print("НОД = {}".format(max(a, b)))
else:
    print("НОK = {}".format(lcm(a, b)))
    print("НОД = {}".format(gcd(a, b)))
