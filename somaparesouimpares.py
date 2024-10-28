def soma_numeros(opcao, limite):
    soma = 0
    if opcao == 'pares':
        for numero in range(1, limite + 1):
            if numero % 2 == 0:
                soma += numero
    elif opcao == 'impares':
        for numero in range(1, limite + 1):
            if numero % 2 != 0:
                soma += numero
    elif opcao == 'todos':
        for numero in range(1, limite + 1):
            soma += numero
    else:
        print("Opção inválida.")
        return
    return soma

# Exemplo de uso
print("Escolha uma opção: 'pares', 'impares' ou 'todos os números'.")
opcao_usuario = input("Opção: ")
limite_usuario = int(input("Até que número? "))
resultado = soma_numeros(opcao_usuario, limite_usuario)
print(f"A soma dos {opcao_usuario} até {limite_usuario} é: {resultado}")
