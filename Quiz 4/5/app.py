def ordenar_crescente(lista):
    """
    Ordena a lista em ordem crescente.
    """
    return sorted(lista)

def ordenar_decrescente(lista):
    """
    Ordena a lista em ordem decrescente.
    """
    return sorted(lista, reverse=True)

# Exemplo de uso
minha_lista = [5, 2, 9, 1, 7]
print("Lista original:", minha_lista)

lista_crescente = ordenar_crescente(minha_lista)
print("Lista em ordem crescente:", lista_crescente)

lista_decrescente = ordenar_decrescente(minha_lista)
print("Lista em ordem decrescente:", lista_decrescente)


def test_ordenacao():
    lista_original = [5, 2, 9, 1, 7]

    # Teste de ordenação crescente
    lista_crescente = ordenar_crescente(lista_original)
    assert lista_crescente == [1, 2, 5, 7, 9]

    # Teste de ordenação decrescente
    lista_decrescente = ordenar_decrescente(lista_original)
    assert lista_decrescente == [9, 7, 5, 2, 1]

    print("Todos os testes passaram!")

# Chame a função de teste
test_ordenacao()