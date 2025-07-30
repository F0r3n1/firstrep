from_currency = input("Введите валюту (USD, EUR, RUB): ").upper()
amount = float(input("Введите сумму: "))
to_currency = input("Введите валюту, в которую хотите перевести сумму (USD, EUR, RUB): ").upper()

rates = {
    "USD": 90.5,
    "EUR": 98.2,
    "RUB": 1
}

def convert(amount, from_currency, to_currency):
    if amount < 0:
        print("Сумма должна быть больше 0!")
        return

    if from_currency not in rates or to_currency not in rates:
        print("Одна из валют неизвестна!")
        return

    if from_currency == to_currency:
        print(f"{amount} {from_currency} = {amount:.2f} {to_currency}")
        return

    if from_currency == "RUB":
        rub_amount = amount
    else:
        rub_amount = amount * rates[from_currency]


    if to_currency == "RUB":
        result = rub_amount
    else:
        result = rub_amount / rates[to_currency]

    print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

convert(amount, from_currency, to_currency)
