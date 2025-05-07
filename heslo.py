import random

zraso = ["Kačenka se Zelím","KnedloVepřoZelo","Vepřová játra na roštu se smaženými hranolky a naší tatarskou omáčkou","Staročeská bašta","Roláda z krůtích stehen, medvědí česnek, bylinky podávaná s pečeným bramborem a glazovanou mrkví"]

v = (random.choice(zraso))

osm = zraso.index(v)

print("Vybral jsem jídlo",v,"co se vybralo","na indexu",osm)

