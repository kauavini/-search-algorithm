# Complexidade: O(log n)

def busca_binaria(array, alvo):
    # Define os índices iniciais e finais para a busca
    inicio = 0
    fim = len(array) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if array[meio] == alvo:
            return meio  
        elif array[meio] > alvo:
            fim = meio - 1
        else:
            inicio = meio + 1

    return -1

array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
alvo = 12
resultado = busca_binaria(array, alvo)

if resultado != -1:
    print(f"O alvo {alvo} foi encontrado no índice {resultado}.")
else:
    print(f"O alvo {alvo} não foi encontrado no array.")
