#Aula 06 - Estrutura de Repetição em Python


#01.Apresente os números pares de um determinado valor - resolver aula
n3 = int(input('Digite um número: '))
for i in range(1, n3):
    if i %2 == 0 :
        print(i)

"""
02.Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:  
5 X 1 = 5  
5 X 2 = 10 
"""

tabuada=int(input("Tabuada do numero: "))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )

#03.Escreva um programa de inverter alguma palavra
palavra = input("Digite uma palavra: ")
palavra_invertida = palavra[::-1]  # Inverte a palavra
print(f"A palavra '{palavra}' ao contrário é: '{palavra_invertida}'")


"""
04. Faça um programa que leia um nome de usuário e a sua senha e 
não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações. 
"""

login = input("Login: ")
senha = input("Senha: ")

while login == senha:
    print("A senha deve ser diferente do login")
    senha = input("Informe novamente uma senha: ")

print("Cadastro aprovado")


"""
05.Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 100;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres). 
"""

nome = input("Qual seu nome [minimo 4 caracteres]: ")
idade = int(input("Sua idade: "))
salario = float(input("Salário: "))
sexo = input("Sexo ('f' para feminino ou 'm' para masculino): ")
civil = input("Estado civil (s, c, v ou d): ")

while len(nome) <= 3:
    nome = input("Seu nome deve ter mais que 3 caracteres: ")

while (idade < 0) or (idade > 100):
    idade = int(input("Voce deve ter entre 0 e 100 anos: "))

while (salario<0):
    salario = float(input("A coisa ta difícil, mas não tem salário negativo: "))

while (sexo!= 'f') and (sexo!='m'):
    sexo = input("Biologicamente, você deve ser 'f' ou 'm': ")

while (civil!='s')and(civil!='c')and(civil!='v')and(civil!='d'):
    print("Nao tem estado civil 'confuso'")
    civil = input("Deve ser s, c, v ou d: ")


#06.Crie um programa em python que adivinha um número de 1 a 10 - resolver aula
import random
numero_adivinhar = random.randint(1,10)


numero_escolhido = 0


while numero_escolhido != numero_adivinhar:
    numero_escolhido = int(input('Adivinhe um número entre 1 e 10: '))
    if numero_escolhido > numero_adivinhar:
        print("Muito alto! Tente novamente.")
    elif numero_escolhido  < numero_adivinhar:
        print("Muito baixo! Tente novamente.")
    else:
        print("Parabéns! Você acertou!!.")

        