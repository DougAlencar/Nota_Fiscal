# Exibe as informações dos alunos;
print("================================================")
print("                  ATIVIDADE 1                   ")
print("------------------------------------------------")
print("Douglas Silva Alencar                           ")
print("------------------------------------------------")

# Exibe o menu de opções dos smartphone;
print("             ESCOLHA O SMARTPHONE               ")
print("================================================")
print("     1 - SAMSUNG S11                            ")
print("     2 - MOTOROLA G8                            ")
print("     3 - iPhone 12                              ")
print("------------------------------------------------")

# Digite a opção de smartphone (1, 2 ou 3), guarde em marca;
marca = int(input("Digite sua escolha: "))
print("------------------------------------------------")

if marca == 1:
    # SAMSUNG S11
    precoBase = 1199.99
    descVista = 0.05
    taxaJuros = 0.10
elif marca == 2:
    # MOTOROLA G8
    precoBase = 1350.00
    descVista = 0.07
    taxaJuros = 0.03
elif marca == 3:
    # iPhone
    precoBase = 3299.99
    descVista = 0.10
    taxaJuros = 0.20
else:
    print("Você escolheu digitar os dados!")
    precoBase = float(input("Digite o preço base para venda........: R$  "))
    descVista = float(input("Digite a taxa de desconto à vista.....: "))
    taxaJuros = float(input("Digite a taxa de juros................: "))

# Apresentação dos preços

# Digitar a forma de pagamento a vista ou parcelado (V ou P), guardar em forma;
# Forma de pagamento
forma = str(input("Pagamento [V} a vista ou [P] parcelado: "))
print("------------------------------------------------")
# Exibir precoBase;
print("Preço base...........: R$ %.2f" % (precoBase))

if (forma == "V") or (forma == "v"):
    valorDesc = precoBase * descVista
    precoFinal = precoBase - valorDesc
    # Exibe precoFinal a vista;
    print("Preço a vista........: R$ %.2f" % (precoFinal))
elif (forma == "P") or (forma == "p"):
    # Digite a quantidade de parcelas, guarde em qtdParc;
    qtdParc = int(input("Digite a quantidade de parcelas: "))
    if qtdParc < 10:
        precoFinal = precoBase
        valorParc = precoFinal / qtdParc
        # Exibe precoFinal parcelado sem juros
        print("Preço final sem juros.: R$ %.2f" % (precoFinal))
    else:
        valorJuros = precoBase * taxaJuros
        precoFinal = precoBase + valorJuros
        valorParc = precoFinal / qtdParc
        # Exibe precoFinal parcelado com juros
        print("Preço final com ", (100*taxaJuros), "%% juros.: R$ %.2f" % (precoFinal))
    #fim-se
    # Exibe valorParc;
    print("Valor de cada parcela.: R$ %.2f" % (valorParc))
else:
    # Exibe Nenhuma forma de pagamento foi selecionada!
    print("Exibe Nenhuma forma de pagamento foi selecionada")
# Fim-se

# Exibe “Fim da execução do programa!”
print("------------------------------------------------")
print("Fim da execução do programa!")
print("================================================")