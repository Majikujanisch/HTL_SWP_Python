import knotandlist
import random
if __name__ == "__main__":
    list = knotandlist.KnotList()

    for i in range(5):
        list.AddToBack(random.randint(0, 100))
    list.ShowList()
    list.InsertAfter(2, 1001)
    list.ShowListwithStart()
    print(str(list.Find(100)))
    list.DeleteAfter(2)
    list.ShowListwithStart()