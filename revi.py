'''1 - Escreva um programa que solicite ao usuário um número inteiro positivo
e realize uma contagem regressiva a partir desse número até zero,
imprimindo cada número no processo.'''

# num_Positivo = int(input("Informe um numéro inteiro positivo: "))
# for i in range (num_Positivo, 0, -1):
#     print(i)

'''2 - Escreva um programa que solicite ao usuário um número inteiro e
imprima a tabuada desse número, de 1 a 10.'''

# mult = 0
# num_int = int(input("Informe um número inteiro para tabuada:  "))
# for i in range (1,11):
#     mult = i * num_int
#     print(f"{num_int} x {i} = {mult} ")

'''3 - Escreva um programa que solicite ao usuário uma frase e conte
quantas vogais (a, e, i, o, u) existem nessa frase.'''
# cont_vogais = 0
# palavra = input("Informe uma frase em questão: ").lower()
# for letra in palavra:
#     if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
#         cont_vogais += 1
# print(f'A quantidade de vogais é {cont_vogais}')

'''4 - Escreva um programa que possa verificar uma sequência de 10
números se são par ou ímpar.'''

impar = 0
par = 0
contador = 0
while contador < 10:
    num = int(input("Informe um número: "))
    if num % 2 == 0:
        par += 1
        print("Os números na sequencia são pares")
    elif num % 2 != 0:
        impar += 1
        print('Os números da sequência são impares')
        contador += 1
        break
        

# '''5 - Hora de otimizar a questão número 3, após ter criado seu programa que
# conta quantas vogais existem numa frase, implemente mais uma
# funcionalidade. O programa agora deve imprimir a quantidade de vogais e
# consoantes encontradas.'''

# cont_consoant = 0 
# cont_vogais = 0
# palavra = input("Informe uma frase em questão: ").lower()
# for letra in palavra:
#      if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
#           cont_vogais = cont_vogais + 1
#      elif letra != "a" or letra != "e" or letra != "i" or letra != "o" or letra != "u":
#           cont_consoant = cont_consoant + 1
# print(f"A quantidade de vogais é: {cont_vogais}, e a de consoantes: {cont_consoant}.")

''''''
