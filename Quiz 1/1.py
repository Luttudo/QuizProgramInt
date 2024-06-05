import re

def validar_senha(senha):
    # Verifica se a senha tem pelo menos 6 e no máximo 32 caracteres
    if len(senha) < 6 or len(senha) > 32:
        return "Senha invalida."

    # Verifica se a senha contém pelo menos uma letra maiúscula, uma letra minúscula e um número
    if not re.search(r'[A-Z]', senha) or not re.search(r'[a-z]', senha) or not re.search(r'\d', senha):
        return "Senha invalida."

    # Verifica se a senha não contém caracteres de pontuação, acentuação ou espaço
    if re.search(r'[^\w\d]', senha):
        return "Senha invalida."

    return "Senha valida."

# Exemplo de uso:
senha = input("Digite a senha: ")
print(validar_senha(senha))
