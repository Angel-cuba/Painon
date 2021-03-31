# Testaan sutty.py:n funktioiden toiminnot

# Modulien ja kirjastojen
import suttu

# Testataan syötettä
def test_kysy_henkilotiedot(monkeypatch):
    syote = 'mika vainio'

    # Korvataan Pythonin sisäinen input-funktio muuttujalla syöte
    monkeypatch.setattr('builtins.input', lambda _: syote)

    assert suttu.kysy_henkilotiedot() == 'Mika Vainio'

def test_totemus(capsys):
    suttu.totemus()
    naytto, virhe = capsys.readouterr()
    assert naytto == 'Kyllä se siitä, herra Angel\n'
    assert virhe == ''