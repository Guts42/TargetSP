n = int(input('Insira um numero a ser buscado na sequência de Fibonnaci: '))
print('-'*40)
t1, t2, t3 = 0, 1, 0
print('{} -> {}'.format(t1, t2), end = '')
while t3 < n:
   t3 = t1 + t2
   print(' -> {}'.format(t3), end = '')
   t1 = t2
   t2 = t3
else:
    print('\n'+'-'*40)
    if(t3 == n):
        print('O número {} pertence a sequência de Fibonacci'.format(n))
    else:
        print('O número {} não pertence a sequência de Fibonacci'.format(n))