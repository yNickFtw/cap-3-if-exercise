import os

week_days = {
    "segunda-feira": 0,
    "terça-feira": 0,
    "quarta-feira": 0,
    "quinta-feira": 0,
    "sexta-feira": 0
}

def print_most_voted_day():
    most_voted_day = max(week_days, key=week_days.get)
    
    print(f"O dia mais votado foi: {most_voted_day.capitalize()}")

def choose_collaborators_number():
    return int(input("Defina o número de colaboradores que irão participar da votação: "))

def choose_day(collaboratorNumber):
        while True:
            choosed_day = input(f"Colaborador {collaboratorNumber}, digite o nome do dia da semana de sua preferência: ")
            if choosed_day.lower() in week_days:
                return choosed_day.lower()
            else:
                print("Dia inválido. Por favor, digite um dia da semana válido.")


def main():
    collaboratorsNumber = choose_collaborators_number()

    while collaboratorsNumber <= 0:
        print("Número inválido")

        choose_collaborators_number()

    def start_voting():
        collaborators_already_voted_count = 0
      
        while collaborators_already_voted_count < collaboratorsNumber:
            print("-------------------------------------")

            for index, day in enumerate(week_days):
                print(f"{index + 1} - {day}")

            choosed_day = choose_day(collaboratorNumber=collaborators_already_voted_count + 1)
            
            week_days[choosed_day] += 1
        
            collaborators_already_voted_count += 1

            os.system('cls')
            
        print_most_voted_day()

    start_voting()

main()