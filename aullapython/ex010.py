real=float(input('Quanto de dinheiro você tem na carteira? R$'))   
dolar=real/5.26 
euro=real/5.61
yen=real/0.038
libra=real/6.23
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar €{:.2f}'.format(real, euro))
print('Com R${:.2f} você pode comprar ¥{:.2f}'.format(real, yen))
print('Com R${:.2f} você pode comprar £{:.2f}'.format(real, libra))