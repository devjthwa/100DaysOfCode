# no_of_books =
# books = 
class Library :
    def __init__(self,name,num_of_books):
        self.name = name
        self.num_of_books = num_of_books
        self.books = []
    def add_book(self,book):
        self.books.append(book)
        self.num_of_books = self.books.length

    def details(self):
        print(f"{self.name} has {self.num_of_books} books")
        print(f"The library has {self.books} books")
book1 = Library("The Secret", 500)
book2 = Library("Life of the Monk", 530)
book3 = Library("Swami Vivekanand", 600)

book1.details()
book2.details()
book3.details()
