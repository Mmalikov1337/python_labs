a = int(input('a = '))
b = int(input('b = '))
 
step = 0
while a != 0 and b != 0:
    step += 1
    if a > b:
        a = a % b
    else:
        b = b % a
 
print(a+b, step)