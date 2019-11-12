from datetime import datetime

class Document:
    def __init__(self, name="", author=""):
        self.name = name
        self.author = author
        self.created = datetime.now()
        self.pages = []

    def add_page(self, page):
        self.pages.append(page)

    def remove_page(self, page):
        self.pages.remove(page)

    def remove_page_by_page_number(self, page_number):
        """
        Uklanja stranicu iz dokumenta na osnovu njenog broja.
        Podrazumevamo da korisnik pocinje brojanje strana od 1.
        Stranice gledamo kao redni broj u dokumentu, a ne redni broj
        koji je zapisan na samoj stranici (njen atribut)
        """
        del self.pages[page_number-1]