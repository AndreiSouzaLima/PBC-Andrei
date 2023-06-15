print('------------------------')
print('pet chop')
print('------------------------')
atendidos = int(input('cãe atendidos:'))
final_de_semana = input('final de semana (S/N):')
if final_de_semana:
    if atendidos <= 20 and atendidos >= 40:
        print('fracasso')
    else:
        print('sucesso')
else:
    if atendidos <= 20 and atendidos >= 30:
        print('fracasso')
    else:
        print('sucesso')