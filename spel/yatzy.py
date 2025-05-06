import random
def slå_tärningar():
    antal_tärningar=0
    mina_tärningar = []
    while antal_tärningar<5:
        mina_tärningar.append(random.randint(1, 6))
        antal_tärningar=antal_tärningar+1
    return mina_tärningar
print(slå_tärningar())



