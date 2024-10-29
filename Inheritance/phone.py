class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.price = price
        self.model = model

    def print_details(self):
        print(f"Brand {self.brand}, Model {self.model}, Price {self.price}")

class Storage:
    def __init__(self):
        self.files = []

    def add_file(self, file):
        self.files.append(file)

    def list_files_in_storage(self):


phone = Phone(Nokia, 8110, 200)
