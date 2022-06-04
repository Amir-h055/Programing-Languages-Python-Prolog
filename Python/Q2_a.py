#Q2a
def F2(n):
    l=[]
    if n >= 0:
        l.append(2)
    if n >= 1:
        l.append(1)

    x, y, z = 2, 1, 0
    for i in range(2,n):
            z = (x + y)
            x, y = y, z
            l.append(y)
    return l
n = int(input("\nEnter number: "))
print("\n" + str(F2(n)))
