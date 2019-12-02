num1 = int(input('Digite o primeiro número: '))
operad = input('Digite o operador + - * / ** % : ')
num2 = int(input('Digite o segundo número: '))


if (operad == "+"):
    result = num1 + num2
elif operad == '-':
    result = num1 - num2
elif operad == '*':
    result = num1 * num2
elif operad == '/':
    result = num1 // num2
    resto = num1 % num2
elif operad == '**':
    result = num1 ** num2
else:
    result = 0


if result == 0:
    print('Operador inválido')
elif operad == '/':
    print()
    print(f'===> Resultado =  {num1} {operad} {num2} = {result} e sobra: {resto}')

else:
    print()
    print(f'===> Resultado =  {num1} {operad} {num2} = {result} ')
