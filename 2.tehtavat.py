nimet = str(input('Anna nimi: '))
lista = set()
lista.add(nimet)

while nimet !="":
    nimet = input('Anna uusi nimi tai lopeta painamalla Enter: ')
    if nimet in lista:
        print("Aiemmin syotetty nimi.")
    else:
        lista.add(nimet)
        print("Uusi nimi.")

for n in lista:
    print(n)