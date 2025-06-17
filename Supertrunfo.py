import random

# Lista de cartas
cartas = [
    {"nome": "Cavaleiro", "forca": 8, "velocidade": 5, "magia": 3},
    {"nome": "Mago", "forca": 4, "velocidade": 6, "magia": 9},
    {"nome": "Dragão", "forca": 9, "velocidade": 7, "magia": 6},
    {"nome": "Orc", "forca": 7, "velocidade": 4, "magia": 2}
]

# Escolhe uma carta aleatória para o jogador e para o computador
carta_jogador = random.choice(cartas)
carta_computador = random.choice([c for c in cartas if c != carta_jogador])

print("Sua carta é:")
for atributo, valor in carta_jogador.items():
    if atributo != "nome":
        print(f"{atributo.capitalize()}: {valor}")
print(f"Nome: {carta_jogador['nome']}")

# Jogador escolhe o atributo
atributo_escolhido = input("Escolha um atributo para disputar (forca, velocidade ou magia): ").lower()

# Mostra as cartas e compara
print(f"\nA carta do computador é: {carta_computador['nome']}")
print(f"{atributo_escolhido.capitalize()} do jogador: {carta_jogador[atributo_escolhido]}")
print(f"{atributo_escolhido.capitalize()} do computador: {carta_computador[atributo_escolhido]}")

# Resultado
if carta_jogador[atributo_escolhido] > carta_computador[atributo_escolhido]:
    print("\nVocê venceu! 🏆")
elif carta_jogador[atributo_escolhido] < carta_computador[atributo_escolhido]:
    print("\nVocê perdeu. 😢")
else:
    print("\nEmpate! ⚔️")
