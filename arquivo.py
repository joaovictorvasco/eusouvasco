import random

def cumprimento(texto):
    return f"Olá, {texto}"

# Chamando a função com o nome completo do aluno
print(cumprimento("Nome Completo do Aluno"))

def sorteia_media():
    numeros = [random.randint(1, 100) for _ in range(3)]
    media = sum(numeros) / 3
    return media

# Chamando a função que sorteia 3 números aleatórios e calcula a média
print(f"A média dos três número sorteados é: {sorteia_media()}")