from random import randint

threeDigit = randint(100, 999)
summa = sum([int(k) for k in str(threeDigit)])

print(f"random three-digit number: {threeDigit}\nsumma: {summa}")