# Tiedostojen luomisen ja käyttämisen kokeiluja

# Kirjastojen ja modulien lataukset 
import os

# print(dir(os))

# Luodaan tiedosto projektin juurihakemistoon
""""
tiedosto = open('data.txt', 'x')
tiedosto.close()
"""

# Lisätään tiedoston uusi rivi
tiedosto = open('data.txt', 'a')
tiedosto.write('# Tässä teidostossa on painoindeksitietoja')
tiedosto.close()

# Luetaan tiedosto
tiedosto = open('data.txt', 'r')
print(tiedosto.read())

# Kirjoitetaan tiedostoon lisää rivejä käyttäen with open() -rakennetta
with open('data.txt', 'a') as tallentaja:
    tallentaja.writelines('Etunimi; Sukunimi; Pituus; Paino\n')
    tallentaja.writelines('Angel;Araoz;177;101\n')
    tallentaja.writelines('Vera;Kapanen;160;70\n')

# Luetaan tiedot with open()
with open('data.txt', 'r') as lukija:
    print(lukija.read())