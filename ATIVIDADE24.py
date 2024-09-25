# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.

n = int(input("Digite um número "))

soma = 0
divisao = 0

while n != -1:
    soma = soma+n
    divisao = divisao+1
    n = int(input('Digite um número '))
    if n == -1:
        break

if n == -1:
    soma += -1
    divisao += 1

media = soma/divisao

print(f'a media dos numeros é {media}')