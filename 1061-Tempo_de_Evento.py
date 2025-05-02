
#1061 - Tempo de um evento
#print("Esse programa fornecerá o tempo que falta para um evento.")

dia_atual = input()
dia_atual = int(dia_atual.split(" "))
#lendo: hora, minuto e segundo
h_atual,m_atual,s_atual = map(int,input().split(" : "))
#print(h_atual,m_atual,s_atual)
dia_evento = input()
dia_evento = int(dia_evento.split()[1])
h_evento,m_evento,s_evento = map(int,input().split(" : "))
#calculo dias
if dia_evento != dia_atual:
    dif_dia = abs((dia_atual + 1) - dia_evento)
else: dif_dia = 0
# calculo horas
if h_evento > h_atual:
    dif_hora = h_evento - h_atual        
elif (dif_dia == 0) and (h_evento == h_atual):
    dif_hora = 0
    dif_dia += 1       
else:
    dif_hora = (24 - h_atual) + h_evento
#calculo minutos
if m_evento < m_atual:
     dif_m = (m_evento + 60) - m_atual
     dif_hora -= 1
else:
     dif_m = m_evento - m_atual
#calculo segundos
if s_evento < s_atual:
     dif_s = (s_evento + 60) - s_atual
     dif_m -= 1
else:
     dif_s = s_evento - s_atual
print(f"{dif_dia} dia(s)")
print(f"{dif_hora} hora(s)")
print(f"{dif_m} minuto(s)")
print(f"{dif_s} segundo(s)")
