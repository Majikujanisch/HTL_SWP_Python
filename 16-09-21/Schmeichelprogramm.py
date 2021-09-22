import random
#Schmeichelprogramm zum Üben
nomen = ['Mensch', 'Behinderter', 'Katze', 'Thomas']
adjektiv = ['schönste', 'intelligenteste', 'klügste', 'lieblichste']
print('du bist der ' + random.choice(adjektiv) + ' ' + random.choice(nomen))
print()
#Zahlenratespiel zum Üben
number = random.randint(1,100)
durchgange = 0
print('Rate die Zahl:')
while durchgange < 7:
