import time
class Knot:
    def __init__(self, value=None, behind=None, next=None):
        self.Behind = behind
        self.Next = next
        self.Value = value

    # in case of testing
    def __str__(self):
        return "Value= " + str(self.Value)

    def GetNextKnot(self):
        return self.Next

    def GetValue(self):
        return self.Value

    def SetValue(self, value):
        self.Value = value


class KnotList:
    def __init__(self):
        self.Start = Knot()
        self.End = Knot(behind=self.Start)
        self.Start.Next = self.End
        self.added = False

    def __len__(self):
        return self.CountListElements()

    def __getitem__(self, index: int):
        return self.FindIndex(index)

    def __setitem__(self, index: int, value):
        knot = self.FindIndexKnot(index)
        knot.Value = value

    def AddToBack(self, value):
        if (self.added == False):

            self.added = True
            knotNewLast = Knot(value=value, behind=self.Start, next=self.End)
            self.Start.Next = knotNewLast
            self.End.Behind = knotNewLast
        else:
            knotOldLast = self.FindLast()
            knotNewLast = Knot(value=value, behind=knotOldLast, next=self.End)
            knotOldLast.Next = knotNewLast
            self.End.Behind = knotNewLast

    def FindLast(self):
        lastknot = self.End.Behind
        return lastknot

    def FindFirst(self):
        return self.Start.Next

    def ShowListwithStart(self):
        searchknot = self.Start
        print(searchknot)
        while (searchknot.GetNextKnot() != self.End):
            searchknot = searchknot.GetNextKnot()
            print(searchknot)
        print(self.End)

    def ShowList(self):
        searchknot = self.Start
        while (searchknot.GetNextKnot() != self.End):
            searchknot = searchknot.GetNextKnot()
            print(searchknot)

    def CountListElements(self):
        index = 0
        searchknot = self.Start
        while (searchknot.GetNextKnot() != self.End):
            searchknot = searchknot.GetNextKnot()
            index = index + 1
        return index

    def AddToStart(self, value):
        if (self.added == False):
            self.added = True
            knotNewLast = Knot(value=value, behind=self.Start, next=self.End)
            self.Start.Next = knotNewLast
            self.End.Behind = knotNewLast
        else:
            knotOldFirst = self.FindFirst()
            knotNewFirst = Knot(value=value, behind=self.Start, next=knotOldFirst)
            knotOldFirst.Behind = knotNewFirst
            self.Start.Next = knotNewFirst

    def DelByValue(self, value):
        searchknot = self.Start
        while (searchknot.GetNextKnot() != self.End):
            searchknot = searchknot.GetNextKnot()
            oldsearchknot = searchknot
            if (searchknot.Value == value):
                searchknotBehind = searchknot.Behind
                searchknotNext = searchknot.Next
                searchknotBehind.Next = searchknotNext
                searchknotNext.Behind = searchknotBehind

    def InsertBefore(self, int, value):
        searchknot = self.Start
        incrementer = 0
        while (incrementer < int - 1):
            searchknot = searchknot.GetNextKnot()
            incrementer = incrementer + 1
        beforeinsertknot = searchknot
        afterinsertknot = searchknot.GetNextKnot()
        newKnot = Knot(value, beforeinsertknot, afterinsertknot)
        beforeinsertknot.Next = newKnot
        afterinsertknot.Behind = newKnot

    def InsertAfter(self, int, value):
        searchknot = self.Start
        incrementer = 0
        while (incrementer < int):
            searchknot = searchknot.GetNextKnot()
            incrementer = incrementer + 1
        beforeinsertknot = searchknot
        afterinsertknot = searchknot.GetNextKnot()
        newKnot = Knot(value, beforeinsertknot, afterinsertknot)
        beforeinsertknot.Next = newKnot
        afterinsertknot.Behind = newKnot

    def DeleteBefore(self, int):
        searchknot = self.Start
        incrementer = 0
        while (incrementer < int - 2):
            searchknot = searchknot.GetNextKnot()
            incrementer = incrementer + 1
        beforedeleteknot = searchknot
        deletionknot = searchknot.GetNextKnot()
        afterdeleteknot = deletionknot.GetNextKnot()
        beforedeleteknot.Next = afterdeleteknot
        afterdeleteknot.Behind = beforedeleteknot

    def DeleteAfter(self, int):
        searchknot = self.Start
        incrementer = 0
        while (incrementer < int):
            searchknot = searchknot.GetNextKnot()
            incrementer = incrementer + 1
        beforedeleteknot = searchknot
        deletionknot = searchknot.GetNextKnot()
        afterdeleteknot = deletionknot.GetNextKnot()
        beforedeleteknot.Next = afterdeleteknot
        afterdeleteknot.Behind = beforedeleteknot

    def FindValue(self, value):
        searchknot = self.Start
        incrementer = 0
        while (searchknot.GetNextKnot() != self.End):
            searchknot = searchknot.GetNextKnot()
            if (searchknot.Value == value):
                incrementer = incrementer + 1
        if (incrementer == 0):
            return -1
        return incrementer

    def FindIndex(self, index):
        searchknot = self.Start
        incrementer = 0
        while incrementer != index:
            searchknot = searchknot.GetNextKnot()
            incrementer = incrementer + 1
        return searchknot.Value

    def FindIndexKnot(self, index):
        searchknot = self.Start
        incrementer = 0
        while incrementer != index:
            searchknot = searchknot.GetNextKnot()
            incrementer = incrementer + 1
        return searchknot

    def SortAsc(self):
        for i in range(1, len(self) + 1):
            key = self.FindIndex(i)
            j = i - 1

            while j >= 1 and key < self.FindIndex(j):
                knot = self.FindIndexKnot(j + 1)
                knot.Value = self.FindIndex(j)
                j -= 1
            knot = self.FindIndexKnot(j + 1)
            knot.Value = key

    def SortDesc(self):
        for i in range(1, len(self) + 1):
            key = self.FindIndex(i)
            j = i - 1

            while j >= 1 and key > self.FindIndex(j):
                knot = self.FindIndexKnot(j + 1)
                knot.Value = self.FindIndex(j)
                j -= 1
            knot = self.FindIndexKnot(j + 1)
            knot.Value = key

    def FillTime(self, it):
        timebefore = time.time()
        for i in range(len(it)):
            self.AddToBack(it[i])
        timeafter = time.time()
        return timeafter-timebefore
    def SortAscTest(self):
        index = 0
        for i in range(1, len(self) + 1):
            key = self.FindIndex(i)
            j = i - 1

            while j >= 1 and key < self.FindIndex(j):
                knot = self.FindIndexKnot(j + 1)
                knot.Value = self.FindIndex(j)
                j -= 1
                index+=1
            knot = self.FindIndexKnot(j + 1)
            knot.Value = key
        return index
    def SortTimeAsc(self):
        before = time.time()
        index = self.SortAscTest()
        after = time.time()
        return index, after-before
    def DefineO(self, length, index):
        return index/length

