# Calculadora de fatorial: Criar um programa que calcule o fatorial de um número fornecido pelo usuário usando um loop while

numero = int(input("Digite um número: "))
fatorial = 1
contador = 1

while (contador <= numero):
    fatorial *= contador #fatorial = fatorial * contador 
    contador += 1 #contador = contador + 1

print(f"o fatorial de {numero} é {fatorial}")