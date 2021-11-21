from random import randint

a = int(input('a: '))
b = int(input('b: '))

while b <= a:
    b = int(input('b must be greater than a, b: '))

print("5 random numbers:")
for i in range(0, 5):
    print(randint(a, b))