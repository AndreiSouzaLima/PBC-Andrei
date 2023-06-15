letra = str(input('Digite uma letra: ')).upper()
if (letra == 'A') or (letra == 'E') or (letra == 'I') or (letra == 'O') or (letra == 'U'):
    print(f'A letra {letra} é uma vogal. ')
else:
    print(f'A letra {letra.upper()} é uma consoante. ')