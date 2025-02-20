from app.models.book import Book, db

class BookRepository:
  @staticmethod
  def get_all_books():
    return Book.query.all()

  @staticmethod
  def get_book_by_id(book_id):
    return Book.query.get(book_id)

  @staticmethod
  def create_book(title, author, price):
    new_book = Book(title=title, author=author, price=price)
    db.session.add(new_book)
    db.session.commit()
    return new_book

  @staticmethod
  def update_book(book_id, title, author, price):
    book = Book.query.get(book_id)
    if book:
      book.title = title
      book.author = author
      book.price = price
      db.session.commit()
    return book

  @staticmethod
  def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
      return None
  
    db.session.delete(book)
    db.session.commit()
    return True
