import csv

import files


def filereader():
    listrows = []
    with open('../names.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in spamreader:
            listrows.append(row)
    return listrows


def filewrite(Choice, winlose):
    listprevrows = filereader()
    with open('../names.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for x in range(len(listprevrows)):
            writer.writerow(listprevrows[x])
        writer.writerow(str(Choice) + str(winlose))


def dataAuswertung():
    data = filereader()
    wins, loses, draw = gameoutgocounter(data)
    schere, stein, papier, echse, spock = signcounter(data)

    print("wins: " + str(wins) + " loses: " + str(loses) + " draws: " + str(draw))
    print("Schere: " + str(schere) + " Stein: " + str(stein) + " Papier: " + str(papier) +
           " Echse: " + str(echse) + " Spock: " + str(spock))
    return gameoutgocounter(data), signcounter(data)

def gameoutgocounter(datalist):
    wins = 0
    loses = 0
    draw = 0
    # go through list and count
    for x in datalist:
        if int(x[1]) == 0:
            wins = wins + 1
        elif int(x[1]) == 1:
            loses = loses + 1
        else:
            draw = draw + 1

    return wins, loses, draw


def signcounter(datalist):
    schere = 0
    stein = 0
    papier = 0
    echse = 0
    spock = 0
    # count signs
    # 0=stein, 1=papier, 2=schere, 3=spock, 4=echse
    for x in datalist:
        sign = int(x[0])
        if sign == 0:
            stein = stein + 1
        elif sign == 1:
            papier = papier + 1
        elif sign == 2:
            schere = schere + 1
        elif sign == 3:
            spock = spock + 1
        elif sign == 4:
            echse = echse + 1
        else:
            print("wrong input")

    return schere, stein, papier, echse, spock
