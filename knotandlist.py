import gc


class Knot:
    def __init__(self, value=None, behind=None, next=None):
        self.Behind = behind
        self.Next = next
        self.Value = value

    #in case of testing
    def __str__(self):
        return "Value= " + str(self.Value)

    def GetNextKnot(self):
        return self.Next

class KnotList:
    def __init__(self):
        self.Start = Knot("Start")
        self.End = Knot("End", behind = self.Start)
        self.Start.Next = self.End
        self.added = False
    def AddToBack(self, value):
        if(self.added == False):

            self.added = True
            knotNewLast = Knot(value=value, behind=self.Start, next=self.End)
            self.Start.Next = knotNewLast
            self.End.Behind = knotNewLast
        else:
            knotOldLast = self.FindLast()
            knotNewLast = Knot(value = value, behind = knotOldLast, next = self.End)
            knotOldLast.Next = knotNewLast
            self.End.Behind = knotNewLast
    def FindLast(self):
        lastknot = self.End.Behind
        return lastknot
    def FinfFirst(self):
        return self.Start.Next
    def ShowList(self):
        searchknot = self.Start
        #print(searchknot)
        while (searchknot.GetNextKnot() != self.End):

            searchknot = searchknot.GetNextKnot()
        print(self.End)

    def CoutnListElements(self):
        index = 0
        searchknot = self.Start
        while (searchknot.GetNextKnot() != self.End):
            searchknot = searchknot.GetNextKnot()
            index = index+1
        print("Anzahl: " + str(index))

    def AddToStart(self, value):
        if (self.added == False):
            self.added = True
            knotNewLast = Knot(value=value, behind=self.Start, next=self.End)
            self.Start.Next = knotNewLast
            self.End.Behind = knotNewLast
        else:
            knotOldFirst = self.FinfFirst()
            knotNewFirst = Knot(value=value, behind=self.Start, next=knotOldFirst)
            knotOldFirst.Behind = knotNewFirst
            self.Start.Next = knotNewFirst

    def DelByValue(self, value):
        searchknot = self.Start
        while (searchknot.GetNextKnot() != self.End):
            searchknot = searchknot.GetNextKnot()
            oldsearchknot = searchknot
            if(searchknot.Value == value):
                searchknotBehind = searchknot.Behind
                searchknotNext = searchknot.Next
                searchknotBehind.Next = searchknotNext
                searchknotNext.Behind = searchknotBehind
    def DelByElemInt(self, value):
        pass







