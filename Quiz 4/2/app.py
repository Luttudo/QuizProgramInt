class CurrencyConverter:
    def __init__(self):
        self.rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'BRL': 5.3  # Exemplo: 1 dólar americano = 5,3 reais
        }

    def convert(self, from_currency, to_currency, amount):
        converted_amount = amount * self.rates[to_currency] / self.rates[from_currency]
        return round(converted_amount, 2)

if __name__ == "__main__":
    converter = CurrencyConverter()
    from_country = input("From Country (USD, EUR, BRL, etc.): ")
    to_country = input("To Country (USD, EUR, BRL, etc.): ")
    amount = float(input("Amount: "))
    result = converter.convert(from_country, to_country, amount)
    print(f"{amount} {from_country} = {result} {to_country}")
