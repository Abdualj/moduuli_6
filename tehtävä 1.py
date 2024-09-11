import random

# Parametriton funktio, joka palauttaa satunnaisen nopan silmäluvun väliltä 1 ja 6
def heita_noppa():
    return random.randint(1,6)

#pääohjelma
def paohjelma():
    while True:
        silmaluku = heita_noppa()
        print(f"silmäluvun tulos : {silmaluku}")
        if silmaluku ==6:
            break

#kutsutaan pääohjelmaa
paohjelma()