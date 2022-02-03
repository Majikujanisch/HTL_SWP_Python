import knotandlist
import random
if __name__ == "__main__":
    list = knotandlist.KnotList()
    for i in range(10):
        list.AddToBack(random.randint(0, 100))
    list.ShowList()
    list.CoutnListElements()
    list.DelByValue(20)
    list.CoutnListElements()
    list.InsertAfter(5, 1001)
    list.ShowList()