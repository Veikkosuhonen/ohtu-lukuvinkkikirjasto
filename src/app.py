from loopbreak import LoopBreak
from book_browser import BookBrowser

class App():
    def __init__(self, io, service):
        self.io = io
        self.service = service
        self.browser = BookBrowser(io, service)

    def run(self):
        self.io.output("Tervetuloa vinkkisovellukseen! Kirjoita \"q\" poistuaksesi sovelluksesta, " +
                       "\"l\" lisätäksesi kirjavinkin, tai \"p\" tulostaaksesi kirjavinkit.")
        command_dict = {"q": self.quit_program,
                        "l": self.add_book,
                        "p": self.print_books}

        self.io.loop(command_dict)

    def quit_program(self):
        raise LoopBreak

    def add_book(self):
        name = self.io.input("Syötä kirjan nimi:\n")
        author = self.io.input("Syötä kirjailijan nimi:\n")
        isbn = self.io.input("Syötä kirjan ISBN-koodi:\n")
        publication_year = self.io.input("Syötä kirjan julkaisuvuosi:\n")
        
        self.service.create_book_tip(name, author, isbn, publication_year)
        self.io.output("Kirja lisätty")

    def print_books(self):
        if len(self.service.get_all_book_tips()) == 0:
            print("Ei vinkkejä")
        for book in self.service.get_all_book_tips():
            print(book, "\n")

    def browse_books(self):
        self.browser.run()
