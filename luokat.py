# Tässä modulissa määritellän luokat painonhallintasovellukseen


# Modulien ja kirjastojen lataukset



# Henkilö-luokka    

class Henkilo:
    """Yliluokka kaikille henkilötyypeille"""
    def __init__(self, etunimi, sukunimi, pituus, paino, ika, sukupuoli):

        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.pituus = pituus
        self.paino =paino
        self.ika = ika
        self.sukupuoli = sukupuoli

    def painoindeksi(self):
        bmi = self.paino / (self.pituus / 100) ** 2
        # print('Painoindeksi on', bmi)
        return bmi

    
    def bmi(pituus, paino):
        bmi = paino / (pituus/ 100)**2
        return bmi

   
class Aikuinen(Henkilo):
    """Aliluokka aikuiselle henkilölle, perii Henkilo-luokan ominaisuudet ja metodit"""
    def __init__(self, etunimi, sukunimi, pituus, paino, ika, sukupuoli, tavoitepaino):
        super().__init__(etunimi, sukunimi, pituus, paino, ika, sukupuoli)
        self.tavoitepaino = tavoitepaino
        

    def rasvaprosentti(self):
        # bmi = self.paino / (self.pituus / 100) ** 2
        rasvaprosentti = 1.2 * self.painoindeksi() + 0.23 * self.ika -10.8 * self.sukupuoli - 5.4
        return rasvaprosentti
    
    

if __name__ == '__main__':
    angel = Henkilo('Angel', 'Araoz', 177, 100, 36, 1)
    print('Henkilö painaa', angel.paino)

    angel.painoindeksi()

    angel2 = Aikuinen('Angel', 'Araoz', 177, 100, 36, 1, 97)
    print(angel2.etunimi, 'painoindeksi', angel2.painoindeksi())
    print(angel2.etunimi,'rasvaprosentti',angel2.rasvaprosentti())

    # Lasketaan painoindeksi staattisella metodoilla
    pituus = 177
    paino = 75

    print('Painoindeksi on:', Henkilo.bmi(pituus, paino))