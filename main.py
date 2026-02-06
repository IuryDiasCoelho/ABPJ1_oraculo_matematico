print("Bem vindo ao oraculo matematico \n"
      "Calculadora de fatura de Energia \n"
      "Vamos começar")
print("______________________________________________________________________________ ")

# entrada de dados do usuario para o mes atual
mes_atual=input("Digite quantos kilovats de energia foi consumido (apenas os valores. EX:350,2): ")

# tratando erro de usar virgula como separador de casas decimais
mes_atual_limpo = float(mes_atual.replace(',', '.'))
preco_kw=(input("Digite preço atual do kilowatt (apenas os valores. EX: 0.89 foi o preço medio em Goiás): "))
preco_kw_limpo=float(preco_kw.replace(',', '.'))

# calculando o valor total do mes atual
cauculo_mes_atual=mes_atual_limpo*preco_kw_limpo
print(f"O seu consumo foi de : {mes_atual_limpo} kilowats")
print(f"O seu preço atual do kilowats foi de : R${preco_kw_limpo}")
print(f"O seu valor total foi da sua fatura atual foi : R${cauculo_mes_atual}")

print("______________________________________________________________________________")

print(f"Faremos um comparativo com o valor do mes anterior para saber a economia ou prejuizo entre os meses")

print("______________________________________________________________________________")

# entrada de dados do usuario para o mes anterior e tratando erro de usar virgula como separador de casas decimais
mes_anterior=input("Digite quantos kilovats foi consumido no mes anterior (apenas os valores. EX:350,2): ")
mes_anterior_limpo = float(mes_anterior.replace(',', '.'))

# calculando o valor total do mes anterior
cauculo_mes_anterior=mes_anterior_limpo*preco_kw_limpo

print(f"O seu valor total foi da sua fatura anterior foi : R${cauculo_mes_anterior}")

# cauculando porcentagem entre os valores
percentagem=(cauculo_mes_atual-cauculo_mes_anterior)/cauculo_mes_anterior*100
perentagem_final=abs(percentagem)

print("______________________________________________________________________________")

if percentagem<0:
    print(f"O seu percentual de prejuizo foi de : {perentagem_final}%")
else:
    print(f"O seu percentual de economia foi de : {perentagem_final}%")

print("_________________________________FIM DO PROGRAMA_____________________________________________")

print("""
           ██████████████████████
      ███████████████████████████████
   █████████████████████████████████████
 █████████████████████████████████████████
███████████████       ███       ███████████
███████████████       ███       ███████████
███████████████████████████████████████████
████████████  ███████████████████  ████████
███████████    █████████████████    ███████
███████████     ███████████████     ███████
 ██████████                         ██████
   ██████████████████████████████████████
      █████████████████████████████████
           █████████████████████████
""")