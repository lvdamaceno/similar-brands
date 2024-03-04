from collections import Counter
from difflib import get_close_matches

def encontrar_repeticoes_palavras_parecidas(lista_palavras):
    # Contar a frequência das palavras na lista
    contagem_palavras = Counter(lista_palavras)

    # Encontrar palavras repetidas
    repeticoes = {palavra: frequencia for palavra, frequencia in contagem_palavras.items() if frequencia > 1}

    # Encontrar palavras parecidas
    palavras_parecidas = {}
    for palavra in lista_palavras:
        matches = get_close_matches(palavra, lista_palavras, n=2, cutoff=0.7)
        if len(matches) > 1:
            palavras_parecidas[palavra] = matches

    return repeticoes, palavras_parecidas


# Exemplo de utilização
if __name__ == "__main__":
    lista_palavras = [
        'BRITANIA',
        'BRITTANIA',
        'OXIGENIO',
        'SEVEN EPIS',
        'THOR MOVEIS',
        'ANTONINI COMERCIAL',
        'CENTRO ELETRONICO',
        'CORD',
        'G5Tech',
        'MIX EPIS',
        'NOVO HORIZONTE',
        'STECK',
        'ALEM DA ARTE',
        'BENCAFIL',
        'BLACK & DECKER',
        'FULLWAY',
        'GALVANIZADO',
        'JOWANEL',
        'POLIFLOR',
        'SOL INFORMATICA',
        'STRETCH',
        'WINGERT',
        'AGRATTO',
        'CINTILANTE'
    ]

    repeticoes, palavras_parecidas = encontrar_repeticoes_palavras_parecidas(lista_palavras)

    print("Palavras repetidas:")
    for palavra, frequencia in repeticoes.items():
        print(f"{palavra}: {frequencia} vezes")

    print("\nPalavras parecidas:")
    for palavra, similares in palavras_parecidas.items():
        print(f"{palavra}: {similares}")

