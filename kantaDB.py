# Tietokantamoduli

# Modulien ja kirjastojen lataukset
import sqlite3

# Luodaan uusi tietokanta projektin hakemistoon
tietokanta = 'painohallinta.db'

def luo_tietokanta(tiedosto):
    """Luo tietokannan huom. tiedoston projektin hakemistoon

    Args:
        tiedosto (string): SQL Tietokantatiedoston nimi
    """
    yhteys = sqlite3.connect(tiedosto)
    yhteys.close()


def luo_taulut(tietokanta):
    """Luo SQL Lite tietokantaan tarvittavat taulut
    """  

    yhteys = sqlite3.connect(tietokanta)

    # Luodaan Henkilö
    yhteys.execute('''CREATE TABLE henkilo(
                                henkilo_id INTEGER PRIMARY KEY NOT NULL, 
                                etunimi TEXT NOT NULL,
                                sukunimi TEXT NOT NULL,
                                sukupuoli INTEGER NOT NULL,
                                spaiva DATE NOT NULL)
                            ''') 
            # Luodaan Mittaukset -taulu
    yhteys.execute('''CREATE TABLE mittaus(
                                mittaus_id INTEGER PRIMARY KEY, 
                                henkilo_id INTEGER NOT NULL, 
                                pituus REAL NOT NULL, 
                                paino REAL NOT NULL)  
                            ''')
    # Suljetaan tietokantayhteys taulujen luonnin jälkeen
    yhteys.close()      

# Luodaan testidataa


#  Paikallisen testaus
if __name__ == '__main__':
    # pass
   # luo_taulut()
   luo_tietokanta(tietokanta)
   luo_taulut(tietokanta)
