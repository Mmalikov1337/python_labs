a = int(input('a = '))
b = int(input('b = '))

step = 0
while a != b:
    step += 1
    if a > b:
        a = a - b
    else:
        b = b - a
print(a, step)
