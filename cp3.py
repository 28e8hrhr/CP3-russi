temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

maior_criticos = 0
sala_maior = 0

# 1. Percorra toda a matriz de temperaturas.
for i in range(len(temperaturas)):
    sala = temperaturas[i]

    # 2. Calcule a média de temperatura de cada sala.
    media = sum(sala) / len(sala)

    # 3. Identifique quantas vezes cada sala registrou temperatura maior ou igual a 33.
    criticos = 0
    for temp in sala:
        if temp >= 33:
            criticos += 1

    # 4. Mostre, para cada sala:
    # - número da sala;
    # - média das temperaturas;
    # - quantidade de registros críticos.
    print(f"Sala {i + 1}")
    print(f"Média das temperaturas: {media:.2f}")
    print(f"Quantidade de registros críticos: {criticos}")
    print("-" * 30)

    # 5. Ao final, informe qual sala teve a maior quantidade de registros críticos.
    if criticos > maior_criticos:
        maior_criticos = criticos
        sala_maior = i + 1


print(f"A sala com maior quantidade de registros críticos foi a Sala {sala_maior}")
print(f"Total de registros críticos: {maior_criticos}")