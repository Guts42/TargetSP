str = input('Digite a frase a ser invertida: ')
str_invertida = []
i = len(str)
while i > 0:
    str_invertida += str[i-1]
    i-=1
str_final = ''.join(str_invertida)
print('A string invertida é:', str_final)