nimet = str(input('Anna nimi: '))
lista = set(nimet)
nimet.__add__(nimet)


nimet = input('Anna uusi nimi tai lopeta painamalla Enter: ')
if nimet in lista:
    print("Aiemmin syotetty nimi.")
elif nimet not in lista:
    print("Uusi nimi.")
elif nimet != "":



print(lista)