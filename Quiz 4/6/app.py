def contar_palavras(texto):
    """
    Conta o número de palavras em um texto.

    Args:
        texto (str): O texto de entrada.

    Returns:
        int: O número de palavras no texto.
    """
    # Divide o texto em palavras usando espaços como delimitadores
    palavras = texto.split()
    return len(palavras)

# Testes unitários
def test_contar_palavras():
    assert contar_palavras("Olá, mundo!") == 2
    assert contar_palavras("Este é um exemplo de texto com várias palavras.") == 8
    assert contar_palavras("Python é incrível!") == 3

if __name__ == "__main__":
    test_contar_palavras()
    print("Todos os testes passaram!")
