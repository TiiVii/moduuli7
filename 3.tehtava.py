def yritys():
    kusumus = input('Aloita kirjoittamalla ALOITA: ')

    asemat = {'EFHK':'Helsinki-Vantaa',
            'EFHA':'Halli',
            'EFJY':'Jyvaskyla',
             'EFOU':'Oulu',
            'EFTU':'Turku'}

    while kusumus != "":
        kusumus = input('Haluatko syotaa uuden lentoaseman UUSI-komennolla,\netsi jo olemassa olevaa HAKU-sanalla tai lopeta ohjelma painamalla Enter: ')
        if kusumus == "HAKU":
            haku = input('Anna ICAO-koodi: \n')
            if haku == "":
                break
            if haku in asemat:
                print(f'ICAO-koodilla {haku} loytyi {asemat[haku]}')
            if haku not in asemat:
                print('Antamaasi ICAO-koodillista lentoasemaa ei loydy.')
        elif kusumus == 'UUSI':
            ICAO = input('Anna uusi ICAO-koodi: ').upper()
            nimi = input('Anna uusi lentoasema: ').capitalize()
            asemat[ICAO] = nimi
            print('Kiitos uudesta lisayksesta.')
            if ICAO == "":
                return


yritys()