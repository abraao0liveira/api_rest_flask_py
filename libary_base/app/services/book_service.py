from app.repositories.book_repository import BookRepository

class BookService:
  @staticmethod
  def list_books():
    return BookRepository.get_all_books()

  @staticmethod
  def get_book(book_id):
    return BookRepository.get_book_by_id(book_id)

  @staticmethod
  def add_book(title, author, price):
    return BookRepository.create_book(title, author, price)

  @staticmethod
  def update_book(book_id, title, author, price):
    return BookRepository.update_book(book_id, title, author, price)

  @staticmethod
  def delete_book(book_id):
    return BookRepository.delete_book(book_id)
