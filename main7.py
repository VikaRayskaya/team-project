def vvod():
    print('Введите последовательность чисел, оканчивающуюся словом "end"')
    A = list(map(str, input().split()))
    A.pop()
    if check(A):
        return A
    else:
        return vvod()
def check(A):
    k = True
    for s in A:
        for ss in s:
            if ss not in '1234567890':
                k = False
    if not k:
        print('Введите корректные данные')
    return k
A = vvod()
for i in range(len(A)):
    A[i] = int(A[i])
kol = 1
prev = A[0]
max_kol = 1
for i in A[1:]:
    chislo = i
    if chislo==prev:
        kol += 1
    else:
        if kol>max_kol:
            max_kol = kol
            ans = prev
        kol = 1
    prev = chislo
if kol>max_kol:
    max_kol = kol
    ans = prev
print('Наибольшее количество подряд идущих равных чисел:',max_kol)
print('Значение числа:',ans)