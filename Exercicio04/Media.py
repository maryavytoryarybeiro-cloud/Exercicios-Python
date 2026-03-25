nota_A = float(input("Informe a primeira nota: "))
nota_B = float(input("Informe a segunda nota: "))

#calcular media
media_final = (nota_A + nota_B) / 2

#verificação
if media_final >=7.0:
    print("A média: %.1f - Aprovado"% media_final)
else:
    print("A média: %.1f - Reprovado "% media_final)