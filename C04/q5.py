class Publisher:
    "information about the class"
    def __init__(self,publisher):
        self.publisher=publisher      
    def display(self):
        pass
class Book(Publisher):
    def __init__(self,publisher,title,author):
        Publisher.__init__(self,publisher)
        self.title=title
        self.author=author
    def display(self):
        pass    
class Python(Book):
    def __init__(self,publisher,title,author,price,pages):
        Book.__init__(self,publisher,title,author)
        self.price=price
        self.pages=pages
    def display(self):
        print("publisher name:",self.publisher)
        print("title:",self.title)
        print("author:",self.author)
        print("price:",self.price)
        print("pages:",self.pages)
s1=Python("Penguin Random House India","Python Basics","Jacob George",1000,500)
s1.display()
