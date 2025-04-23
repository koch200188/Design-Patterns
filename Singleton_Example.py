class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("Erstellt eine neue Singleton Instanz")
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = 0
        else:
            print("Verwende existierende Singleton Instanz")
        return cls._instance
    
    def increment(self):
        self.value += 1
        return self.value

print("Erste Instanz erstellen:")
s1 = Singleton()
print(f"Wert von s1: {s1.value}")

print("\nZweite Instanz erstellen:")
s2 = Singleton()
print(f"Wert von s2: {s2.value}")

print("\nÜberprüfen, ob s1 und s2 die gleiche Instanz sind:")
print(f"s1 ist s2: {s1 is s2}")

print("\nWert in s1 erhöhen:")
s1.increment()
print(f"Neuer Wert von s1: {s1.value}")
print(f"Wert von s2 (sollte auch erhöht sein): {s2.value}")