#ALUNO: ADALBERTO DA SILVA ALMEIDA

# CALCULADORA DE MÉDIA ACADÊMICA #

'''solicitar os dados do aluno'''

aluno = str(input("Informe o primeiro nome do aluno:")) # Recebe o nome do aluno.
nota1 = float(input("Informe a primeira nota do aluno:")) # Recebe a primeira nota.
nota2 = float(input("Informe a segunda nota do aluno:")) # Recebe a segunda nota.

'''Mostrar a média do aluno'''

media = (nota1 + nota2) / 2 # Faz o calculo da média
print("A média final de %s é %f." % (aluno,media)) # Imprime a média do aluno.


'''Verificar o estatus dos aluno e a média final'''

if media < 4.0: # Verifica se a média é menor que 4.
    print("%s foi REPROVADO." %aluno)
elif media >=4.0 and media < 7.0: # Verifica se a média do aluno é iguau ou maior que 4 e menor que 7.
    minMedia = 5 - media
    if minMedia < 4.0:
        minMedia = 4.0
    print("%s deverá fazer a prova final e a média minima é %f." % (aluno, minMedia))
else: # Caso a media não atenda aos requisitos anteriores ela será maior que 7 logo o else será executado.
    print("%s foi APROVADO." %aluno)