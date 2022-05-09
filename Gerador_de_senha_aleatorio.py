from random import choice
import string

print('Gerador de Senha aleatório')
tamanho = int(input('Digite o tamanho que deseje que sua senha possua: '))

valores = string.ascii_letters + string.digits
senha = ''
for i in range(tamanho):
  senha += choice(valores)

print('sua senha é: '+ senha)