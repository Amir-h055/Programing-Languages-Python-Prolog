def F(n):
    if n == 0: return 2
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

n = int(input("How many numbers to generate: "))
for i in range(n - 1):
    print(F(i), end=' ')
