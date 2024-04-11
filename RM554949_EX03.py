def main():
    installments = {
        1: 0,
        3: 10,
        6: 15,
        9: 20,
        12: 25
    }
    
    debt_value = float(input("Digite o valor da divida: ")) 
    
    for installment in installments.items():
        value_to_add = debt_value * (installment[1] / 100)
        
        total_value = value_to_add + debt_value 

        installment_value = total_value / installment[0]
        
        print(f"Total: R$ {total_value} Juros: {value_to_add} Número de parcelas: {installment[0]} Valor da parcela: {installment_value:.2f}")
    
    
main();