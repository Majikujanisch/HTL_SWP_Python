import knotandlist
import random
if __name__ == "__main__":
    list = knotandlist.KnotList()

    for i in range(5):
        list.AddToBack(random.randint(0, 100))
    list.ShowList()
    list.ShowListwithStart()
    list.ShowList()
    list.CoutnListElements()
    list.DelByValue(20)
    list.CoutnListElements()
    print("del done")
    list.ShowList()
    list.InsertAfter(2, 1001)
    list.ShowList()
    list.ShowListwithStart()