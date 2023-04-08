print('CALCULADORA')
print('+ ADIÇÃO')
print('- SUBTRAÇÃO')
print('* MULTIPLICAÇÃO')
print('/ DIVISÃO')
print('Pressione outra tecla para sair')

op = input('Qual operação deseja fazer? ')
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))

if(op == '+'):
  res = x + y
  print(f'O resultado do valor {x} + {y} = {res}')

elif(op == '-'):
    res = x - y
    print(f'O resultado do valor {x} - {y} = {res}')

elif (op == '*'):
    res = x * y
    print(f'O resultado do valor {x} * {y} = {res}')

elif(op == '/'):
    res = x / y
    print(f'O resultado do valor {x} / {y} = {res}')
else:
    print('Operação invalida')

print('Encerrando o programa')