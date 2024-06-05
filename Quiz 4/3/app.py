def is_secure_password(password):
    # Verifica o comprimento mínimo
    if len(password) < 8:
        return False

    # Verifica se há pelo menos 1 letra maiúscula, 1 letra minúscula e 1 dígito
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    if not (has_upper and has_lower and has_digit):
        return False

    # Verifica se há pelo menos 1 caractere especial
    special_chars = "!@#$%^&*()_+{}[]|;:,.<>?~"
    has_special = any(c in special_chars for c in password)
    if not has_special:
        return False

    return True

# Exemplo de uso
user_password = input("Digite a senha: ")
if is_secure_password(user_password):
    print("Senha segura!")
else:
    print("Senha não atende aos critérios de segurança.")
