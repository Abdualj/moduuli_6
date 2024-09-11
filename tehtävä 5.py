# Funktio, joka poistaa listasta parittomat luvut ja palauttaa uuden listan
def poista_parittomat(luvut):
    return [luku for luku in luvut if luku % 2 == 0]


# Pääohjelma
def paohjelma():
    # Luodaan lista kokonaisluvuista
    alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Kutsutaan funktiota ja tallennetaan karsittu lista
    karsittu_lista = poista_parittomat(alkuperainen_lista)

    # Tulostetaan alkuperäinen ja karsittu lista
    print(f"Alkuperäinen lista: {alkuperainen_lista}")
    print(f"Karsittu lista (vain parilliset luvut): {karsittu_lista}")


# Kutsutaan pääohjelmaa
paohjelma()
