n1 = int(input('Digite um Numero: '))

def fizzbuzz(n1):
    if n1 % 2 == 0 and n1 % 5 == 0:
        print('FizzBuzz')
    elif n1 % 2 == 0:
        print('Fizz')
    else:
        print('Buzz')

fizzbuzz(n1)