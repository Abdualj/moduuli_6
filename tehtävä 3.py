# Funktio, joka muuntaa gallonat litroiksi
def gallonat_litroiksi(gallonat):
    return gallonat * 3.785


# Pääohjelma
def paohjelma():
    while True:
        gallonat = float(input("Anna bensiinin määrä nestegallonoina (negatiivinen luku lopettaa): "))

        # Lopetetaan ohjelma, jos käyttäjä syöttää negatiivisen arvon
        if gallonat < 0:
            print("Ohjelma lopetettu.")
            break

        litrat = gallonat_litroiksi(gallonat)
        print(f"{gallonat} nestegallonaa on {litrat:.2f} litraa.")


# Kutsutaan pääohjelmaa
paohjelma()
