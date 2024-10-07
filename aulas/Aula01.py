nome = input('Digite o seu nome:')
print('Muito prazer {}!'.format(nome))


#soma de dois números
numero1 = int(input('Digite o número 1: '))
numero2 = int(input('Digite o número 2: '))
resultado = numero1 + numero2
print('A soma dos dois número é igual: {}'.format(resultado))


#antecessor e sucessor
numero = int(input('Digite um número: '))
a = numero - 1
b = numero + 1
print('O número {} tem como antecessor {} e tem como sucessor {}'.format(numero, a, b))


#dobro, triplo e raiz
# vamos usar a variavel numero
dobro = numero*2
triplo = numero*3
raiz = (numero**(1/2))
print('O número {} tem como dobro {} tem como triplo {} e como raiz quadrada {:.2f}'.format(numero, dobro, triplo, raiz))


#resolver aula - média aritmética
#


#resolver aula - Escreva um programa que pergunte a quantidade de KM percorridos
#por um carro alugado e a quantidade de dias pelo quais ele foi alugado.
#calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por KM rodado.
#
#


#for
n = int(input('Digite um número: '))
for i in range(0, n):
    print(f"Os números até o {n} são: {i}")


#while
n2 = int(input('Digite um número: '))
while n2 >=0:
    print(n2)
    n2 -=1
    