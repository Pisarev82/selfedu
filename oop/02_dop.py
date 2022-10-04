fib1 = 0
fib2 = 1

n = int(input("Введите число "))


result = str(fib1) + ' ' + str(fib2)
for i in range(1, n + 1):
    fib1, fib2 = fib2, fib1 + fib2
    # print(fib2, end=' ')
    if i == n and i % 2 != 0:
        result = str(fib1) + ' ' + result
    elif i % 2 == 0 and i != n:
        result = str(-fib1) + ' ' + result + ' ' + str(fib2)
    elif i == n and i % 2 == 0:
        result = str(-fib1) + ' ' + result
    else:
        result = str(fib1) + ' ' + result + ' ' + str(fib2)
print(result)