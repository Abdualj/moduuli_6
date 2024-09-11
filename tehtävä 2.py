import random


# Funktio, joka saa parametrina nopan tahkojen määrän ja palauttaa satunnaisen silmäluvun
def heita_noppaa(tahkot):
    return random.randint(1, tahkot)


# Pääohjelma
def paohjelma():
    # Kysytään käyttäjältä, kuinka monta tahkoa nopassa on
    tahkot = int(input("Anna nopan tahkojen määrä: "))

    while True:
        silmaluku = heita_noppaa(tahkot)
        print(f"Silmäluvun tulos: {silmaluku}")
        if silmaluku == tahkot:
            break


# Kutsutaan pääohjelmaa
paohjelma()
