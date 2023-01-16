A = int(input('digite o 1 lado do triângulo:'))
B = int(input('digite o 2 lado do triângulo:'))
C = int(input('digite o 3 lado do triângulo:'))

if (A > 0) and (B > 0) and (C > 0):
   if (A + B > C) and (A + C > B) and (B + C > A):
    # se vc chegou até aqui, é pq o triangulo é valido
         if A != B and A != C and B != C:
             print('é um triangulo escaleno')
         else:
             if A == B and A == C and B == C:
                 print('triangulo equilátero')
             else:
                print('Triangulo isósceles')

   else:
       print('Um dos valores indicados não serve para formar um triangulo')
else:
   print('Um dos valores indicados não serve para formar um triangulo')
