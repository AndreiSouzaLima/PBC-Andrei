popa = 80000
popb = 200000
cresa = (3/100)
cresb = (1.5/100)
anos = 0
while popa < popb:
    anos += 1
    popa = popa + (popa * cresa)
    popb = popb + (popb * cresb)
print(f'Após {anos} anos o país A obteve uma população de aproximadamente {popa:.0f} habitantes.')
print(f'Superando a população do país B que era de aproximadamente {popb:.0f} habitantes. ')