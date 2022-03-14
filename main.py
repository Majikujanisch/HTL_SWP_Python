import knotandlist
import random
if __name__ == "__main__":
    list = knotandlist.KnotList()

    for i in range(10):
        list.AddToBack(random.randint(0, 100))
    print('\n\n\n================')
    print("show")
    list.ShowListwithStart()
    print(list.FindIndexKnot(1).Value)
    print('\n\n\n================')
    print("sort")
    list.SortAsc()
    print('\n\n\n================')
    list.ShowList()
