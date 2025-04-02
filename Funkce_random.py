import random 

barvy = ["modrá", "červená", "zelená", "fialová","bílá"]
print (barvy)

dalsiBarva = input("Napište nějakou další barvu")

barvy.append (dalsiBarva) 

for i in barvy :
    print(i)

nahodnaHodnota = random.choice(barvy)
print ("Náhodná hodnota je", nahodnaHodnota)
