# Quyidagi parametr va metodlardan foydalanib, Bookcase nomli class yarating. 
#     Dastur ota class va subclasslardan tashqari to’g’ridan to’gri kitobning nomi, 
#     kitoblar soni va kitoblar ro’yxatini ko’rishga yo’l qo’ymasin. 
# Bookcase atributlari: bookname, amount (miqdor), booklist (ro'yxat)
# Bookcase metodlari: bookcase_info(), add_book(), get_book(), show_books()

class Bookcase:
    def __init__(self):
        self.bookname = ""
        self.amount = 0
        self.booklist = []

    def bookcase_info(self):
        print(f"Bookcase ma'lumotlari:\nBook Nomi: {self.bookname}\nMiqdori: {self.amount}\n")

    def add_book(self, bookname, amount):
        self.bookname = bookname
        self.amount += amount
        self.booklist.extend([bookname] * amount)
        print(f"{amount} {bookname} bookcase ga qo'shildi.")

    def get_book(self):
        if self.amount > 0:
            book = self.booklist.pop()
            self.amount -= 1
            print(f"'{book}' bookcase dan olingan.")
        else:
            print("Bookcase da kitob yo'q.")

    def show_books(self):
        if self.amount > 0:
            print("Bookcaseda mavjud kitoblar:")
            for book in self.booklist:
                print("-", book)
        else:
            print("Bookcase da kitoblar yo'q.")

if __name__ == "__main__":
    bookshelf = Bookcase()
    bookshelf.bookcase_info()
    bookshelf.add_book("Python", 5)
    bookshelf.add_book("Java", 3)
    bookshelf.get_book()
    bookshelf.show_books()
