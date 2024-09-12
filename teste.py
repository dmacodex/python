# Calcular a duração de cada atividade com base nos horários fornecidos

from datetime import datetime, timedelta

# Definir os horários de início e fim para cada atividade
horarios = {
    "Meditar": ("05:00", "07:00"),
    "Exercitar 1": ("07:00", "09:00"),
    "Trabalhar 1": ("09:00", "11:00"),
    "Exercitar 2": ("11:00", "12:30"),
    "Comer 1": ("12:30", "13:00"),
    "Trabalhar 2": ("13:00", "17:00"),
    "Exercitar 3": ("17:00", "18:30"),
    "Comer 2": ("18:30", "19:00"),
    "Exercitar 4": ("19:00", "20:00"),
    "Descansar": ("20:00", "21:00"),
    "Dormir": ("21:00", "05:00")
}

# Função para calcular a duração entre dois horários
def calcular_duracao(inicio, fim):
    formato_hora = "%H:%M"
    hora_inicio = datetime.strptime(inicio, formato_hora)
    hora_fim = datetime.strptime(fim, formato_hora)
    
    # Se a hora de fim for menor, significa que a atividade vai até o próximo dia
    if hora_fim < hora_inicio:
        hora_fim += timedelta(days=1)
    
    return hora_fim - hora_inicio

# Calcular as durações
duracoes = {atividade: calcular_duracao(inicio, fim) for atividade, (inicio, fim) in horarios.items()}
duracoes
