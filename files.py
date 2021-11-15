import csv

import files


def filereader():
    listrows = []
    with open('names.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in spamreader:
            print(row)
            listrows.append(row)
    return listrows

def filewrite(Choice, winlose):
    listprevrows = filereader()
    with open('names.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for x in range(len(listprevrows)):
            writer.writerow(listprevrows[x])
        writer.writerow(str(Choice) + str(winlose))

