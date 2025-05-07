import random

# Vytvoření pole se zvířaty
zvirata = ["pes", "kočka", "myš", "kráva", "kůň"]

# Výběr náhodného zvířete
v7 = random.choice(zvirata)

# Zjištění indexu vybraného zvířete
index = zvirata.index(v7)

# Výpis výsledku
print("Vybral jsem zvíře \"" + v7 + "\" co se vybralo na indexu " + str(index))
