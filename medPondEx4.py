# -*- coding:utf8 -*-

#recebendo valores e pesos
valor1 = int(input('Digite o primeiro valor: '))
peso1 = int(input('Digite o peso do primeiro valor: '))

valor2 = int(input('Digite o segundo valor: '))
peso2 = int(input('Digite o peso do segundo valor: '))

valor3 = int(input('Digite o terceiro valor: '))
peso3 = int(input('Digite o peso do terceiro valor: '))

mp = ((valor1 * peso1) + (valor2 * peso2) + (valor3 * peso3))/(peso1+peso2+peso3)

print("A média ponderada é: ", mp)
