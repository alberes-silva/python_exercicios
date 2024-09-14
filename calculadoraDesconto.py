compra = float(input("Digite o valor da compra: "))
pagamento = int(input("Pagamento à vista: 1-Sim 2-Não "))

if(compra < 800):
  desconto = compra - (compra * 0.05)
  if(pagamento == 1):
    vista = desconto - (desconto * 0.05)
    print("Pagamento à vista R$",vista )
  elif(pagamento == 2):
    print("Valor da compra R$ {}, com desconto de 5% R$ {}".format(compra,desconto))
elif(compra >= 801 and compra <= 1500):
  desconto = compra - (compra * 0.10)
  if(pagamento == 1):
    vista = desconto - (desconto * 0.05)
    print("Pagamento à vista R$",vista )
  elif(pagamento == 2):
    print("Valor da compra R$ {}, com desconto de 10% R$ {}".format(compra,desconto))
else:
  desconto = compra - (compra * 0.20)
  if(pagamento == 1):
    vista = desconto - (desconto * 0.05)
    print("Pagamento à vista R$",vista )
  elif(pagamento == 2):
    print("Valor da compra R$ {}, com desconto de 20% R$ {}".format(compra,desconto))