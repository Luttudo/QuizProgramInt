from datetime import datetime

def calcular_diferenca_entre_datas(data1, data2):
    """
    Calcula a diferença entre duas datas.

    Args:
        data1 (str): Data no formato "dd/mm/aaaa".
        data2 (str): Data no formato "dd/mm/aaaa".

    Returns:
        str: A diferença entre as datas em anos, meses, dias, horas e minutos.
    """
    formato = "%d/%m/%Y"
    data1_obj = datetime.strptime(data1, formato)
    data2_obj = datetime.strptime(data2, formato)

    diferenca = data2_obj - data1_obj
    anos = diferenca.days // 365
    meses = (diferenca.days % 365) // 30
    dias = diferenca.days % 30
    horas, minutos = divmod(diferenca.seconds, 3600)

    return f"{anos} anos, {meses} meses, {dias} dias, {horas} horas e {minutos} minutos."

# Exemplo de uso
data1 = "01/01/2020"
data2 = "15/06/2024"
print(calcular_diferenca_entre_datas(data1, data2))

def test_calcular_diferenca_entre_datas():
    # Teste 1: Diferença de 1 ano, 5 meses, 14 dias, 0 horas e 0 minutos
    data1 = "01/01/2020"
    data2 = "15/06/2021"
    assert calcular_diferenca_entre_datas(data1, data2) == "1 anos, 5 meses, 14 dias, 0 horas e 0 minutos."

    # Teste 2: Diferença de 4 anos, 5 meses, 14 dias, 12 horas e 30 minutos
    data1 = "01/01/2010"
    data2 = "15/06/2014"
    assert calcular_diferenca_entre_datas(data1, data2) == "4 anos, 5 meses, 14 dias, 12 horas e 30 minutos."

    # Teste 3: Diferença de 0 anos, 0 meses, 0 dias, 3 horas e 45 minutos
    data1 = "10/05/2024"
    data2 = "10/05/2024"
    assert calcular_diferenca_entre_datas(data1, data2) == "0 anos, 0 meses, 0 dias, 3 horas e 45 minutos."

if __name__ == "__main__":
    test_calcular_diferenca_entre_datas()
    print("Todos os testes passaram!")

