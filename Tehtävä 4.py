# Funktio, joka laskee listassa olevien kokonaislukujen summan
def laske_summa(luvut):
    return sum(luvut)


# Pääohjelma
def paohjelma():
    # Luodaan lista kokonaisluvuista
    luvut = [1, 2, 3, 4, 5]  # Voit muokata listaa testausta varten

    # Kutsutaan funktiota ja tallennetaan palautettu summa
    summa = laske_summa(luvut)

    # Tulostetaan summa
    print(f"Listan {luvut} summa on: {summa}")


# Kutsutaan pääohjelmaa
paohjelma()
