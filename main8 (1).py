print('Введите число')
n = int(input())
chislo = 2
power = 1
while chislo<=n:
    chislo *= 2
    power += 1
print('Наибольшая степень двойки:',power-1)