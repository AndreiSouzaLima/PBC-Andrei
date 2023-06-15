print('Digite M para matutino ou v para vespertino ou n para noturno. ')
turno = str(input('Em que turno você estuda? ')).upper()
matutino = 'M'
vespertino = 'V'
noturno = 'N'
if turno == matutino:
    print('Bom dia!')
if turno == vespertino:
    print('Boa tarde!')
if turno == noturno:
    print('Boa noite!')
else:
    if turno != matutino:
        if turno != vespertino:
            if turno != noturno:
                print('Valor inválido!')