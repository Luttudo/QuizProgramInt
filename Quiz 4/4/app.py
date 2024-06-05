import re

def is_valid_email(email):
    """
    Verifica se o e-mail fornecido é válido.
    """
    # Expressão regular para validar o formato do e-mail
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Exemplo de uso
user_email = input("Digite o e-mail: ")
if is_valid_email(user_email):
    print("E-mail válido!")
else:
    print("E-mail inválido.")

# Testes unitários
def test_is_valid_email():
    assert is_valid_email("user@example.com")
    assert is_valid_email("john.doe123@gmail.com")
    assert is_valid_email("contact@company.co.uk")
    assert not is_valid_email("invalid-email")
    assert not is_valid_email("user@.com")
    assert not is_valid_email("user@domain")
    assert not is_valid_email("user@domain.")
    assert not is_valid_email("user@.co")
    assert not is_valid_email("user@.co.")
    assert not is_valid_email("user@.com.")
    assert not is_valid_email("user@.com..")


test_is_valid_email()

