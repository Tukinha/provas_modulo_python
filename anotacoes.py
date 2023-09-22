'''1. Faça um programa para imprimir os números de 1 a 10. Utilize a função
range() para criar a coleção de números.'''

# for n in range(1,11):
#     print(n)

'''2. Faça um programa para imprimir os números pares de 1 a 20. Utilize a
função range() para criar a coleção de números.'''

# for n in range(1,21):
#     if n % 2 == 0:
#         print(n)

'''3. Faça um programa para imprimir os números ímpares de 1 a 19. Utilize a
função range() para criar a coleção de números.'''

# for n in range(1, 20):
#    if n % 2 != 0:
#       print(n)

'''4. Faça um programa para calcular a soma dos números de 1 a 100. Utilize a
função range() para criar a coleção de números.'''#*

# atrib = 0
# for i in range(1,101):
#     atrib = atrib + i
#     print(atrib)

'''6. Faça um programa para verificar se um número é primo. Utilize a
condicional IF dentro do laço FOR.'''

# num = int(input("Informe um número: "))
# for i in range (1, num):
#     if num % i == 1 or num % i == num:
#         print("O número é primo")
#         break
#     else :
#         print("Não é primo")

'''8. Faça um programa para contar quantas vogais existem em uma palavra.
Utilize a condicional IF dentro do laço FOR.'''

# c = 0
# palavra = input("Informe a palavra a ser percorrida: ").upper()
# for i in palavra:
#     if i == "a" or i == "e" or i == "o" or i == "u":
#         c += 1
#         print(c)

'''9. Faça um programa para contar quantas consoantes existem em uma
palavra. Utilize a condicional IF dentro do laço FOR.''' #*


# c = 0
# palavra = input("Informe a palavra a ser percorrida: ").upper()
# for i in palavra:
#     if i != "a" or i != "e" or i != "o" or i != "u":
#         c += 1
#         print(c)

'''10. Faça um programa para verificar se uma palavra é um palíndromo.
Exemplo: ‘amor’ = ‘roma’ (NÃO É) / ‘arara’ = ‘arara’ (É PALÍNDROMO).'''

'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:'''

# Tabuada de 5:

# 5 X 1 = 5

# 5 X 2 = 10

# ...

# 5 X 10 = 50

# num_usuario = int(input("informe um número: "))
# for i in range(1, 11):
#  print(f"{num_usuario} x {i} = {i*num_usuario}")
 
'''Escreva um programa em python que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.'''

# numero_cont = 0
# contador = 0
# while True:
#   num = int(input("Informe um número inteiro: "))
#   if num == 0:
#    print(num)
#    contador = contador + 1
#    print(f"Soma: {numero_cont}, média: {numero_cont/contador}")
#    break
#   else: 
#     contador += 1
#     numero_cont += num
    
