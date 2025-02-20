from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  author = db.Column(db.String(100), nullable=False)
  price = db.Column(db.Float, nullable=False)

  def to_dict(self):
    return {
      'id': self.id,
      'title': self.title,
      'author': self.author,
      'price': self.price
    }
