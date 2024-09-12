from datetime import datetime, timedelta

# Definir os horários de início e fim para cada atividade
horarios = {
    "Preparar 1": ("04:00", "04:30"),
    "Trabalhar 1": ("04:30", "07:00"),
    "Exercitar 1": ("07:00", "08:30"),
    "Preparar 2": ("08:30", "09:00"),
    "Trabalhar 2": ("09:00", "11:00"),
    "Exercitar 2": ("11:00", "12:30"),
    "Preparar 3": ("12:30", "13:00"),
    "Comer 1": ("13:00", "13:30"),
    "Trabalhar 3": ("13:30", "17:00"),
    "Exercitar 3": ("17:00", "18:30"),
    "Preparar 4": ("18:30", "19:00"),
    "Comer 2": ("19:00", "19:30"),
    "Preparar 5": ("19:30", "20:00"),
    "Dormir 1": ("20:00", "04:00")
}

# Função para calcular a duração entre dois horários
def calcular_duracao(inicio, fim):
    formato_hora = "%H:%M"
    hora_inicio = datetime.strptime(inicio, formato_hora)
    hora_fim = datetime.strptime(fim, formato_hora)
    
    # Se a hora de fim for menor, significa que a atividade vai até o próximo dia
    if hora_fim < hora_inicio:
        hora_fim += timedelta(days=1)
    
    duracao =  (hora_fim - hora_inicio).total_seconds() / 3600
    return duracao

# Calcular as durações
#duracoes = {atividade: calcular_duracao(inicio, fim) for atividade, (inicio, fim) in horarios.items()}

duracoes = {}
for atividade, (inicio, fim) in horarios.items():
    duracao_atual = calcular_duracao(inicio, fim)
    duracoes[atividade[:-2]] = duracoes.get(atividade[:-2], 0) + duracao_atual

#print(horarios)
print(duracoes)