print('calculadora')
print('+ adição')
print('- subtração')
print('* multiplicação')
print('/ divisão')
print('Pressione outra tecla para encerrar')

op = input('Qual operação queres fazer?')
if op == '+' or op == '-' or op == '*' or op == '/':
  x = int(input('Digite o primeiro valor:'))
  y = int(input('Digite o segundo valor:'))

if (op == '+'):
   res = x + y
   print('resultado = {} + {} = {}'. format(x , y , res))
elif (op == '-'):
   res = x - y
   print('resultado = {} - {} = {}'.format(x, y, res))
elif (op == '*'):
   res = x * y
   print('resultado = {} * {} = {}'.format(x, y, res))
elif (op == '/'):
   res = x / y
   print('resultado = {} / {} = {}'. format(x , y , res))
else:
    print('Vc digitou uma operação invalida')

print('Encerramento do programa')