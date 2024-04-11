def calculate_tax_redemption(investment_type, redemption_value, days_invested):
    if investment_type == 1:  # CDB
        if days_invested <= 180:
            income_tax_rate = 0.225
        elif 181 <= days_invested <= 360:
            income_tax_rate = 0.2
        elif 361 <= days_invested <= 720:
            income_tax_rate = 0.175
        else:
            income_tax_rate = 0.15
        tax_due = redemption_value * income_tax_rate
        return tax_due
    elif investment_type == 2 or investment_type == 3:
        print("Investimento isento de imposto de renda.")
        return 0
    else:
        print("Tipo de investimento inválido.")
        return None


def main():
    investment_type = int(input("Digite o tipo de investimento (1 para CDB, 2 para LCI, 3 para LCA): "))
    if investment_type not in [1, 2, 3]:
        print("Tipo de investimento inválido.")
        return

    redemption_value = float(input("Digite o valor a ser resgatado: "))
    days_invested = int(input("Digite o número de dias que o valor permaneceu investido: "))

    tax_due = calculate_tax_redemption(investment_type, redemption_value, days_invested)
    if tax_due is not None:
        print("Imposto de renda devido:", tax_due)


if __name__ == "__main__":
    main()
