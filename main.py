import knotandlist
import random
if __name__ == "__main__":
    list = knotandlist.KnotList()
    for i in range(1000):
        list.AddToBack(random.randint(0, 100))
    list.ShowList()
    list.CoutnListElements()
    list.DelByValue(20)
    list.CoutnListElements()