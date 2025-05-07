import random
# 1. Vytvoření pole s čísly
pole_cisel = [1,2,3,4,5,6,7,8,9,10]
# Výběr náhodného čísla z pole
v2 = random.choice(pole_cisel)
# Zjištění indexu vybraného čísla
index_v2 = pole_cisel.index(v2)
# Výpis výsledku 
print("Vybral jsem číslo", v2, "na indexu", index_v2, "v poli")