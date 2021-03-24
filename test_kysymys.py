# Kysymysmodulin testit

# ;odulien ja kirjatojen lataukset
import  kysymys

# Syöte ok                          
def test_kysymys_ok():
    kysymys.input = lambda: '50'
    assert kysymys.kysy_liukuluku('Syötä arvo', 10,100) == 50

# Syötteessä  tietotyyppivirhe



# Alle alarajan




# Yli ylärajan