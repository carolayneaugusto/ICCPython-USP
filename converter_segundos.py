total_segs = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = total_segs // 86400
segundos_restantes = total_segs % 86400
horas = segundos_restantes // 3600
segundos_restantes = segundos_restantes % 3600
minutos = segundos_restantes // 60
segundos_finais = segundos_restantes % 60
print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos_finais} segundos.')
