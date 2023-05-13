class library:
    def __init__(self,books):
        self.books = books

    def list_books(self):
        for book in self.books:
            print(book)

    def borrow_book(self,barrow_book):
        if barrow_book in self.books:
            print('get your book')
            self.books.remove(barrow_book)
        else:
            print('book is not available')

    def return_book(self,return_book):
        print('you have returned book')
        self.books.append(return_book)

msg = '''
        1)display books
        2)borrow book
        3)return book
      '''

books = ['c++','java','c']
l1 = library(books)
while(True):
    print(msg)
    num = int(input("enter your choice:"))
    if num==1:
        l1.list_books()
    elif num==2:
        book =  input("enter book name:")
        l1.borrow_book(book)
    elif num==3:
        book = input("enter book name:")
        l1.return_book(book)
    else:
        print("thank you for your visit!!")