real = float(input('Quanto dinheio você tem na carteira? R$:'))
dolar = real/ 3.27
dolar = float(input('quantos dolares voce tem na cateira? U$:'))
euro = dolar/3.27
print('Com R$ {:.2f} você pode comprar US$ {:.2f} ou comprar € {:.2f}'.format(real, dolar))
   