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
    def ShowList(self):
        searchknot = self.Start
        print(searchknot)
        while (searchknot.GetNextKnot() != self.End):

            searchknot = searchknot.GetNextKnot()
            print(searchknot)
        print(self.End)

    def CoutnListElements(self):
        index = 0
        searchknot = self.Start
        while (searchknot.GetNextKnot() != self.End):
            searchknot = searchknot.GetNextKnot()
            index = index+1
        print("Anzahl: " + str(index))






