from flask import Flask
from app.models.book import db
from app.controllers.book_controller import book_controller
from app.config.config import Config

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)
  db.init_app(app)
    
  app.register_blueprint(book_controller)
    
  return app

if __name__ == '__main__':
  app = create_app()
  app.run(debug=True)

