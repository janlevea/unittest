# 
# parillisuus.py(T1_2_2.py) käytetään lukujen parillisuuden tarkistukseen.
# @author tekijä: JaniL
# @since pvm: 18.4.2023
# @version versio: 1.0
#


aloitusInt: int = 0
lopetusInt: int = 0

def kaynnistys():
    print("Tämä ohjelma tulostaa parilliset ja parittomat numerot annetulla alueella.")
    global aloitusInt
    global lopetusInt
    aloitusInt = kysy_aloitusnumero()
    lopetusInt = kysy_lopetusnumero()
    parillisuus(aloitusInt, lopetusInt)

def kysy_aloitusnumero() -> int:
    global aloitusInt
    numeroHyvaksytty: bool = False
    while numeroHyvaksytty == False:
        try:
            aloitusStr = input("Mistä numerosta aloitetaan? ")
            aloitusInt = int(aloitusStr)
            numeroHyvaksytty = True
            return aloitusInt
        except:
            print("Virheellinen syöte. Annoithan pelkän kokonaisluvun?")

def kysy_lopetusnumero() -> int:
    global lopetusInt
    numeroHyvaksytty: bool = False
    while numeroHyvaksytty == False:
        try:
            lopetusStr = input("Mihin numeroon lopetetaan? ")
            lopetusInt = int(lopetusStr)

            if lopetusInt >= aloitusInt:
                numeroHyvaksytty = True
            else:
                print("Virheellinen syöte. Lopetusluvun pitää olla kokonaisluku, joka on suurempi tai yhtäsuuri kuin aloitusluku.")
                numeroHyvaksytty = False
                continue
        except:
            print("Virheellinen syöte. Annoithan pelkän kokonaisluvun?")
            numeroHyvaksytty = False
            continue
        else:
            numeroHyvaksytty = True
            return lopetusInt

def parillisuus(aloitusAlue=0, lopetusAlue=10):
    parilliset = []
    parittomat = []

    if aloitusAlue == lopetusAlue:
        if(aloitusAlue % 2) == 0:
            print(f"Numero {aloitusAlue} on parillinen luku.")
            return
        else:
            print(f"Numero {aloitusAlue} on pariton luku.")
            return
    else:
        for counter in range(aloitusAlue, lopetusAlue+1):
            if(counter % 2) == 0:
                parilliset.append(counter)
            else:
                parittomat.append(counter)

    print(f"Parilliset ({len(parilliset)}kpl): {parilliset}")
    print(f"Parittomat ({len(parittomat)}kpl): {parittomat}")

    return((parilliset, parittomat)) # Tuple jossa molemmat listat, testejä varten


if __name__ == "__main__":
    kaynnistys()