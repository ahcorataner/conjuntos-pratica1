import random

def ler_conjunto_usuario():
    """
    Lê do usuário um conjunto com 4 a 8 elementos inteiros.
    Garante que não haja duplicatas.
    """
    while True:
        try:
            n = int(input("Quantos elementos terá o conjunto A? (4 a 8): "))
            if 4 <= n <= 8:
                break
            else:
                print("Quantidade inválida. Digite um valor entre 4 e 8.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    conjunto = set()
    while len(conjunto) < n:
        elemento = input(f"Digite o elemento {len(conjunto)+1}: ")
        conjunto.add(elemento)

    return conjunto


def gerar_conjunto_aleatorio():
    """
    Gera um conjunto aleatório com 4 a 8 elementos (strings numéricas).
    """
    tamanho = random.randint(4, 8)
    universo = [str(i) for i in range(1, 21)]
    return set(random.sample(universo, tamanho))


def mostrar_operacoes(A, B, U):
    print("\n--- Conjuntos ---")
    print(f"A (usuário): {A}")
    print(f"B (aleatório): {B}")

    print("\n--- Operações ---")
    print(f"A ∪ B = {A.union(B)}")
    print(f"A ∩ B = {A.intersection(B)}")
    print(f"A - B = {A.difference(B)}")
    print(f"B - A = {B.difference(A)}")
    print(f"A Δ B = {A.symmetric_difference(B)}")

    print("\n--- Cardinalidades ---")
    print(f"|A| = {len(A)}")
    print(f"|B| = {len(B)}")
    print(f"|A ∪ B| = {len(A.union(B))}")

    print("\n--- Complementos (em relação ao universo U) ---")
    print(f"U = {U}")
    print(f"Complemento de A = {U.difference(A)}")
    print(f"Complemento de B = {U.difference(B)}")


def main():
    print("=== Atividade Prática – Teoria dos Conjuntos ===")
    A = ler_conjunto_usuario()
    B = gerar_conjunto_aleatorio()

    # Universo definido como a união dos dois conjuntos
    U = A.union(B)

    mostrar_operacoes(A, B, U)


if __name__ == "__main__":
    main()
