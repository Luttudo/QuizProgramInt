# Calculadora Simples

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

# Testes unitários
def test_calculadora():
    assert adicao(2, 3) == 5
    assert subtracao(5, 2) == 3
    assert multiplicacao(4, 3) == 12
    assert divisao(10, 2) == 5
    assert divisao(10, 0) == "Erro: Divisão por zero"

if __name__ == "__main__":
    test_calculadora()
    print("Testes passaram!")
