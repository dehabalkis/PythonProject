#Experiment_Daten_Kapseln_Telefonbuch_besondere Methoden

class PhoneBook():
    
    def __init__(self):
        self.__entries = {}
        
    def add(self, name, phone_number):
        self.__entries[name] = phone_number
        
    def get(self, name):
        if name in self.__entries:
            return self.__entries[name]
        else:
            return None
    def __str__(self):
        return "PhoneBook("+ str(self.__entries)+ ")"
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return len(self.__entries)
    
book = PhoneBook()
book.add("Mustermann" , "+491234567")

#book = PhoneBook()
book.add("deha" , "+491234567")

book.add("ozan" , "+491234567")

#print(book.get ("Mustermann"))

#print(book)

#book

print(len(book))

print(book)
