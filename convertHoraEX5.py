#-*- coding: utf8 -*-

'''
Dado um valor de tempo em segundos (inteiro),
converta-o para o formato horas:minutos:segundos.
'''

segundos = int(input('Digite o valor em segundos: '))

minuto = segundos // 60
hora = minuto // 60
segundo = segundos % 60

print(f"{hora}:{minuto}:{segundo}")
