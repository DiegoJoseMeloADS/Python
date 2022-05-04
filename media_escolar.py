nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))
nota3 = int(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3)/3

print(f'Sua media é de: {media}')

if media >= 6:
    print("Aprovado")
elif media == 5:
    print("Recuperação")
else:
    print("Reprovado")

