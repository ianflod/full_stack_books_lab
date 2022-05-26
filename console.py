import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Dan Brown")
author_repository.save(author1)
author2 = Author("Mary Shelley")
author_repository.save(author2)
author3 = Author("Joe Simpson")
author_repository.save(author3)

book1 = Book("Da Vinci Code", author1)
book_repository.save(book1)
book2 = Book("Frankenstein", author2)
book_repository.save(book2)
book3 = Book("Touching the Void", author3)
book_repository.save(book3)


book_repository.select_all()


