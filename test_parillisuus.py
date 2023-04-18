import parillisuus

# parillisuus, numerot 0-10
def test_parillisuus():
    palautetut_listat = parillisuus.parillisuus(0, 10)
    parilliset = palautetut_listat[0]
    parittomat = palautetut_listat[1]
    assert parilliset == [0, 2, 4, 6, 8, 10]
    assert parittomat == [1, 3, 5, 7, 9]

# parillisuus, numerot 5-21
def test_parillisuus2():
    palautetut_listat = parillisuus.parillisuus(5, 21)
    parilliset = palautetut_listat[0]
    parittomat = palautetut_listat[1]
    assert parilliset == [6, 8, 10, 12, 14, 16, 18, 20]
    assert parittomat == [5, 7, 9, 11, 13, 15, 17, 19, 21]

# Alla olevissa annetaan numero stringinä, tulee palautua inttinä
def test_kysy_aloitusnumero(monkeypatch):
    user_input = "5"
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    palautettuNumero = parillisuus.kysy_aloitusnumero()
    assert palautettuNumero != "5"
    assert palautettuNumero == 5

def test_kysy_aloitusnumero2(monkeypatch):
    user_input = "12"
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    palautettuNumero = parillisuus.kysy_aloitusnumero()
    assert palautettuNumero != "12"
    assert palautettuNumero == 12

def test_kysy_lopetusnumero(monkeypatch):
    user_input = "15"
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    palautettuNumero = parillisuus.kysy_lopetusnumero()
    assert palautettuNumero != "15"
    assert palautettuNumero == 15

def test_kysy_lopetusnumero2(monkeypatch):
    user_input = "128"
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    palautettuNumero = parillisuus.kysy_lopetusnumero()
    assert palautettuNumero != "128"
    assert palautettuNumero == 128