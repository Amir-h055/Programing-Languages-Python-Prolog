#Q2b
def F3(n):
    x, y = 2, 1
    for _ in range(n):
        yield x
        x, y = y, x+y

n = int(input("How many to generate: "))
print(list(F3(n)))
