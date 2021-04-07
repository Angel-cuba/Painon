# Tietokantamoduli

# Modulien ja kirjastojen lataukset
import sqlite3

# Luodaan uusi tietokanta projektin hakemistoon
def luo_tietokanta(tiedosto):
    """Luo tietokannan huom. tiedoston projektin hakemistoon

    Args:
        tiedosto (string): SQL Tietokantatiedoston nimi
    """
    yhteys = sqlite3.connect(tiedosto)
    yhteys.close()


def luo_taulut():
    """Luo SQL Lite tietokantaan tarvittavat taulut
    """  

    yhteys = sqlite3.connect('painohallinta.db')

    # Luodaan Henkilö
    yhteys.execute('''CREATE TABLE henkilo(
                                henkilo_id INTEGER PRIMARY KEY NOT NULL, 
                                etunimi TEXT NOT NULL,
                                sukunimi TEXT NOT NULL,
                                sukupuoli INTEGER,
                                spaiva DATE)
                            ''') 
            # Luodaan Mittaukset -taulu
    yhteys.execute('''CREATE TABLE mittaus(
                                mittaus_id INTEGER PRIMARY KEY, 
                                henkilo_id INTEGER NOT NULL, 
                                pituus REAL NOT NULL, 
                                paino REAL NOT NULL)  
                            ''')
    yhteys.close()      # Luodaan Henkilö-taulu
           
# Luodaan testidataa


#  Paikallisen testaus
if __name__ == '__main__':
    pass
   # luo_taulut()