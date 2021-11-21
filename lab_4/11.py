n = int(input('n: '))

for i in range(1, n):
    a = str(i**2)
    if a[-len(str(i))] == str(i):
        print('afor', i, a)
