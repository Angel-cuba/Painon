# Modulin laskenta.py testit   

# Modulien ja kirjastojen lataukset
import laskenta

# Ensimäinen testi laskentaan painoindeksi ja verratan tulostaa ennalta laskettun arvon
def test_painoindeksi():
    assert laskenta.bmi(74, 1.71) == 20    
