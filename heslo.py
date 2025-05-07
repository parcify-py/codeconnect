import random
smajlici = ["😊", "😊", "😊", "😊", "😊", "😊", "😊", "😊"]
v5 = random.choice(smajlici)
index = smajlici.index(v5)
print(f"Vybral jsem smajlíka {v5} na indexu {index}")


import random
smajlici = ["😊", "😊", "😊", "😊", "😊", "😊", "😊", "😊"]
index = random.randint(0, len(smajlici) - 1)
v5 = smajlici[index]
print(f"Vybral jsem smajlíka {v5} na indexu {index}")
