# -*-coding:utf8-*-

num = int(input('Digite um número: '))

if num >= 0 and num <= 50:
    print('[0,50]')
elif num >= 51 and num <= 100:
    print('[51,100]')
else:
    print('Fora do intervalo')
