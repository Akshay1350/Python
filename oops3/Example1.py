class Book:
    def __init__(self,pages):
        self.pages=pages
        return
    def __add__(self,chetan):
        return "{} pages and {} pages".format(self.pages,chetan.pages)
b1=Book(100)
b2=Book(500)
print(b2+b1)
