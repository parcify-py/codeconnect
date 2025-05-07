import random

operace = ["+","-","*"]
v6 = random.choice(operace)
index = operace.index(v6)

print(f"vybral jsem operaci {v6} na indexu {index}")


znaky = ['#', '@', '%']

v3 = random.choice(znaky)

index = znaky.index(v3)

print("Vybral jsem znak " + v3 + " na indexu " + str(index))

