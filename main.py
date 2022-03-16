import knotandlist
import random
import Arraylist

if __name__ == "__main__":
    zahlen = []
    for i in range(100):
        zahlen.append(random.randint(0,100))
    list = knotandlist.KnotList()
    array = Arraylist.ArrayList(size=1)

    print("Füllzeit Liste")
    print(list.FillTime(zahlen))

    print("Füllzeit ArrayList")
    print(array.FillTime(zahlen))

    print("Sortierzeit Liste")
    OListe, timeListe = list.SortTimeAsc()
    print(timeListe)

    print("Sortierzeit Array")
    OArray, timeArray = array.SortTimeAsc()
    print(timeArray)

    print("Aufwandsklassen")
    print(str(list.DefineO(100, OListe)) + "n")
    print(str(OArray/100) + "n")

