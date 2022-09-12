numero = int(input('Anna kuukauden numero: '))

kuukaudet = ("talvi", "talvi", "kevat", "kevat", "kevat", "kesa", "kesa", "kesa", "syksy", "syksy", "syksy", "talvi")

kuukausi = kuukaudet[numero-1]
print (f'{numero}. Kuukausi on {kuukausi}.')
