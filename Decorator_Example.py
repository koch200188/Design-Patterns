from abc import ABC, abstractmethod

class Kaffee(ABC):
    @abstractmethod
    def kosten(self):
        pass
    
    @abstractmethod
    def beschreibung(self):
        pass

class EinfacherKaffee(Kaffee):
    def kosten(self):
        return 2.0
    
    def beschreibung(self):
        return "Einfacher Kaffee"

class KaffeeDecorator(Kaffee):
    def __init__(self, kaffee):
        self._kaffee = kaffee
    
    def kosten(self):
        return self._kaffee.kosten()
    
    def beschreibung(self):
        return self._kaffee.beschreibung()

class MilchDecorator(KaffeeDecorator):
    def kosten(self):
        return self._kaffee.kosten() + 0.5
    
    def beschreibung(self):
        return self._kaffee.beschreibung() + ", mit Milch"

class ZuckerDecorator(KaffeeDecorator):
    def kosten(self):
        return self._kaffee.kosten() + 0.2
    
    def beschreibung(self):
        return self._kaffee.beschreibung() + ", mit Zucker"

class SahneDecorator(KaffeeDecorator):
    def kosten(self):
        return self._kaffee.kosten() + 0.7
    
    def beschreibung(self):
        return self._kaffee.beschreibung() + ", mit Sahne"

class KaramellDecorator(KaffeeDecorator):
    def kosten(self):
        return self._kaffee.kosten() + 0.8
    
    def beschreibung(self):
        return self._kaffee.beschreibung() + ", mit Karamell"

if __name__ == "__main__":
    mein_kaffee = EinfacherKaffee()
    print(f"{mein_kaffee.beschreibung()} kostet {mein_kaffee.kosten()}€")
    
    mein_kaffee = MilchDecorator(mein_kaffee)
    print(f"{mein_kaffee.beschreibung()} kostet {mein_kaffee.kosten()}€")
    
    mein_kaffee = ZuckerDecorator(mein_kaffee)
    print(f"{mein_kaffee.beschreibung()} kostet {mein_kaffee.kosten()}€")
    
    luxus_kaffee = KaramellDecorator(SahneDecorator(EinfacherKaffee()))
    print(f"{luxus_kaffee.beschreibung()} kostet {luxus_kaffee.kosten()}€")
    
    extrem_kaffee = KaramellDecorator(SahneDecorator(ZuckerDecorator(MilchDecorator(EinfacherKaffee()))))
    print(f"{extrem_kaffee.beschreibung()} kostet {extrem_kaffee.kosten()}€")
    