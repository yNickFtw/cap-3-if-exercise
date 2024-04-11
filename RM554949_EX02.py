def main():
    installments = {
    6: 3,
    12: 6,
    18: 9,
    24: 12,
    30: 15,
    36: 18,
    42: 21,
    48: 24,
    54: 27,
    60: 30
    }

    car_value = float(input('Digite o valor do carro: '))
    
    value_to_discount = car_value * (20 / 100)
    
    final_price = car_value - value_to_discount
    
    print(f"O preço final á vista com desconto de 20% é: {final_price:.2f}")
    
    for installment in installments.items():
        value_to_add = car_value * (installment[1] / 100)
        
        final_value = car_value + value_to_add
        
        installment_value = final_value / installment[0]
        
        print(f"O preço final parcelado em {installment[0]} X é de R$ {final_value:.2f} com parcelas de R$ {installment_value:.2f}")    
    
main()