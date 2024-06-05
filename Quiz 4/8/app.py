import phonenumbers

def validar_numero_telefone(numero):
    """
    Valida se um número de telefone está correto com DDD e número.

    Args:
        numero (str): Número de telefone no formato internacional (exemplo: "+5511987654321").

    Returns:
        bool: True se o número for válido, False caso contrário.
    """
    try:
        numero_obj = phonenumbers.parse(numero)
        return phonenumbers.is_valid_number(numero_obj)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False

# Exemplos de uso
numero1 = "+5511987654321"
numero2 = "+442071234567"
print(validar_numero_telefone(numero1))  # Deve retornar True
print(validar_numero_telefone(numero2))  # Deve retornar True

# Teste inválido (não é um número de telefone válido)
numero_invalido = "12345"
print(validar_numero_telefone(numero_invalido))  # Deve retornar False
