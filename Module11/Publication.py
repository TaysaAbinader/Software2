class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, pages):
        self.author = author
        self.pages = pages
        super().__init__(name)

    def print_info(self):
        print(f"Book name: {self.name}, Author: {self.author}, Page quantity: {self.pages}")

class Magazine(Publication):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)

    def print_info(self):
        print(f"Magazine: {self.name}, Chief Editor: {self.editor}")


magazine1 = Magazine("Donald Duck", "Aki Hyyppä")
book1 = Book("Compartment No. 6", "Rosa Liksom", 192)
magazine1.print_info()
book1.print_info()