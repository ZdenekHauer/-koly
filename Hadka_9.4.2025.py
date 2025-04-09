import random 
nakup = ["máslo", "auto","čokoládu","chleba","deštník","počítač","důn", "pastelky", "telefon", "tablet"] 
nahodnaHodnota = random.choice (nakup)
for i in range (10) :
    print ("Kupme",random.choice (nakup) )
    print ("Ne, kupme", random.choice (nakup ))

