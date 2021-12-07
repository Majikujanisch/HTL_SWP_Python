from enum import Enum
class Firma:
    def __init__(self, personen, abteilungen):
        self.Person = personen
        self.abteilung = abteilungen


    def addPersonToAbteilung(self):
        tempind = 0
        maxind = 0
        maxabtl = 0
        for i in self.abteilung:
            for x in self.Person:
                if x.Mitarbeiter.abteilung == i:
                    tempind = tempind +1
            if tempind > maxind:
                maxabtl = i
        return maxabtl.getName()
    def countMitarbeiter(self):
        index = 0
        for x in self.Person:
            index = index +1
        return index

    def countGruppenleiter(self):
        index = 0
        for x in self.Person:
            if isinstance(x, Gruppenleiter) :
                index  = index +1
        return index

    def countAbteilungen(self):
        index = 0
        for x in self.abteilung:
            index = index + 1
        return index
    def strongestAbteilung(self):
        tempind = 0
        maxind = 0
        maxabtl = 0
        for i in self.abteilung:
            tempind = 0
            for x in self.Person:
                if x.abteilung == i:
                    tempind = tempind + 1
            if tempind > maxind:
                maxabtl = i
                maxind = tempind
        return maxabtl.getName()


        return strogestabteilung
    def percentofWomenMen(self):
        weiblich = 0
        maenlich = 0
        for x in self.Person:
            if x.getGender() == Geschlecht.Weiblich:
                weiblich = weiblich+1
            elif x.getGender() == Geschlecht.Maennlich:
                maenlich = maenlich + 1
        return (weiblich/self.countMitarbeiter()) * 100 , (maenlich/self.countMitarbeiter()) * 100
class Geschlecht(Enum):
    Weiblich = 1
    Maennlich = 2
    Inter = 3
    NotSpecified = 4

class Person:
    def __init__(self, Vorname, Nachname, Alter, Geschlecht):
        self.firstname = Vorname
        self.lastname = Nachname
        self.age = Alter
        self.gender = Geschlecht
    def getGender(self):
        return self.gender

class Mitarbeiter(Person):
    def __init__(self, vorname, nachname, alter, geschlecht, abteilung):
        super().__init__(vorname, nachname, alter, geschlecht)
        self.abteilung = abteilung


class Gruppenleiter(Mitarbeiter):
    def __init__(self, vorname, nachname, alter, geschlecht, abteilung):
        super().__init__(vorname, nachname, alter, geschlecht,abteilung)

class Abteilung:
    def __init__(self, name):
        self.Personen = ()
        self.Name = name
    def addPerson(self, person):
        self.Personen.extend(person)
    def getName(self):
        return self.Name
