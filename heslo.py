import random

zvirata = ["pes", "kočka", "myš", "kráva", "kůň"]

v7 = random.choice(zvirata)

index = zvirata.index(v7)

print("Vybral jsem zvíře \"" + v7 + "\" co se vybralo na indexu " + str(index))
