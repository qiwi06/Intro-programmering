import random
def slå_tärningar(hurmånga_tärningar):
    antal_tärningar=5-hurmånga_tärningar
    mina_tärningar = []
    while antal_tärningar<5:
        mina_tärningar.append(random.randint(1, 6))
        antal_tärningar=antal_tärningar+1
    return mina_tärningar
print(slå_tärningar(5))
sparade_tärningar = []
tärningar= input("Vilka tärningar vill du spara?")
print(tärningar)
sparade_tärningar = tärningar.split()
print(sparade_tärningar)
resterande_tärningar = slå_tärningar(5-len(sparade_tärningar))
print(resterande_tärningar)
tärningar= input("Vilka tärningar vill du spara?")


