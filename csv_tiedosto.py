# Modulin avulla luodaan, luetaan ja kirjoitetaan CSV-tiedostoja

# Kirjastojen ja modulien lataukset
import csv

# Luodaan otsikot CSV-tiedostoon
def luo_otskot(tiedosto):

# Määritellään csv-tiedosto, erotin ja tekstitunnitwe
    with open(tiedosto, mode='w') as datatiedosto:
        csv_kirjoittaja = csv.writer(datatiedosto, dialect='excel', delimiter= ';', quotechar='"')
        csv_kirjoittaja.writerow(['Etunimi', 'Sukunimi', 'Pituus', 'Paino', 'Ikä', 'Sukupuoli', 'Tavoitepaino'])

# Lisätään rivejä CSV-tiedostoon
def luo_otskot(tiedosto, etunimi, sukunimi, pituus, paino, ika, sukupuoli, taivotepaino):
    with open(tiedosto, mode='a') as datatiedosto:
        csv_kirjoittaja = csv.writer(datatiedosto, dialect='excel', delimiter= ';', quotechar='"')
        csv_kirjoittaja.writerow(['etunimi', 'sukunimi', 'pituus', 'paino', 'ika', 'sukupuoli', 'tavoitepaino'])

if __name__ == '__main__':

    # Lisätään testimielessä rivejä
    lisaa_tiedot('bmidata.csv', 'Angel', 'Araoz', '177','101','36', '1', '85')
#    lisaa_tiedot('bmidata.csv', 'Vera', 'Kapanen', '160','70','59', '1', '70')



    with open('bmidata.csv', 'r') as testiluku:
        print(testiluku.read())