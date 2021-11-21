from random import randint

print("random integer from 0 to 100:")
n = randint(0, 100)
t = 10
while t > 0:
    k = int(input("Number: "))
    if k > n:
        print('k > n')
        t -= 1
    elif k < n:
        print('k < n')
        t -= 1
    elif k == n:
        print('you win')
        break
if t <= 0:
    print(f'random number is {n}')