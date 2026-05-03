#ALUNO: ADALBERTO DA SILVA ALMEIDA

# CALCULADORA DE MÉDIA ACADÊMICA #

aluno = str(input("Informe o primeiro nome do aluno:")) # Recebe o nome do aluno.
nota1 = float(input("Informe a primeira nota do aluno:")) # Recebe a primeira nota.
nota2 = float(input("Informe a segunda nota do aluno:")) # Recebe a segunda nota.

media = (nota1 + nota2) / 2 # Faz o calculo da média
print("A média final de %s é %f." % (aluno,media)) # Imprime a média do aluno.

if media < 4.0:
    print("%s foi REPROVADO." %aluno)
elif media >=4.0 and media < 7.0:
    print("%s deverá fazer a prova final." %aluno)
else:
    print("%s foi APROVADO." %aluno)