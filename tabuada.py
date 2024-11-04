#O usuário vai inserir um número
contador = 0
n1 = int(input("Digite um número para ver sua tabuada: "))


#O código exibira a tabuada 
while (contador <= 10):
    resultado = n1 * contador 
    print (f"{n1} x {contador} = {resultado}")
    contador += 1
