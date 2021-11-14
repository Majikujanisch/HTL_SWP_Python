import csv

def filewriter(Choice, winlose):
    with open('names.csv', 'w', newline='') as csvfile:
        listChoice = Choice
        listgameoutgo= winlose
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for x in len(listChoice):
            writer.writerow({listChoice[x] + ' ' + listgameoutgo[x]})

def filereader():

    with open('names.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    for row in spamreader:
        print(', '.join(row))