import random
print "use speech marks to enter information."
player1=input("What is the name of the first player? ")
player2=input("What is the name of the second player? ")
print player1
p1type=input("Choose a damage type. PSYCHIC FIRE OR DARKNESS. Type first letter. ")
if p1type=="p":
  print "you selected PSYCHIC"
if p1type=="f":
  print "you selected FIRE"
if p1type=="d":
  print "you selected DARKNESS"
print player2
p2type=input("Choose a damage type. DARKNESS FIRE OR POISON. Type first letter. ")
if p2type=="p":
  print "you selected PSYCHIC"
if p2type=="f":
  print "you selected FIRE"
if p2type=="d":
  print "you selected DARKNESS"
print "BEGIN THE FIGHT"
print player1, "your turn!"
