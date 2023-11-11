'''
Вводится натуральное число n. По данному числу выведите:
Сумму кубов – 13 + … + n3
Сумму факториалов – 1! + … + n!
'''
n = int(input())
kub = 0
fact = 1
sum_fact = 0
for i in range(1,n + 1,1):
    kub += i * i * i
    fact = fact * i
    sum_fact += fact

print("Сумма кубов", kub)
print("Сумму факториалов", sum_fact)