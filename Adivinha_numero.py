import random

numero = random.randint(1,10)

print("Tente adivinhar o numero de 1 a 10")

palpite = int(input("De o um palpite:"))

if palpite == numero :
    print("Parabens")
else:
    while palpite != numero :
       palpite = int(input("Tente denovo: "))
    else:
        print("Parabens")
