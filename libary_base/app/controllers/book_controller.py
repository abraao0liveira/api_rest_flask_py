from flask import Blueprint, jsonify, request
from app.services.book_service import BookService
from app.config.response_model import response_model

book_controller = Blueprint('book_controller', __name__)


@book_controller.route('/api/books/listall', methods=['GET'])
def list_all_books():
  try:
    books = BookService.list_books()
    books_data = [book.to_dict() for book in books]

    return response_model(200, message='Livros listados com sucesso', data=books_data)
  
  except Exception as e:
    return response_model(400, message='Erro ao listar livros', error=str(e))


@book_controller.route('/api/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
  try:
    book = BookService.get_book(book_id)
    if book:
      return response_model(200, message='Livro encontrado', data=book.to_dict())
    
  except Exception as e:
    return response_model(400, message='Erro ao buscar livro', error=str(e))


@book_controller.route('/api/books/add', methods=['POST'])
def add_book():
  try:
    data = request.get_json()

    if 'title' not in data or 'author' not in data or 'price' not in data:
      return response_model(400, message='Dados inválidos', error='Campos obrigatórios: title, author, price')
    
    new_book = BookService.add_book(data['title'], data['author'], data['price'])

    return response_model(201, message='Livro adicionado com sucesso', data=new_book.to_dict())
  
  except Exception as e:
    return response_model(400, message='Erro ao adicionar livro', error=str(e))


@book_controller.route('/api/books/update/<int:book_id>', methods=['PUT'])
def update_book(book_id):
  try:
    data = request.get_json()

    if 'title' not in data or 'author' not in data or 'price' not in data:
      return response_model(400, message='Dados inválidos', error='Campos obrigatórios: title, author, price')
    
    updated_book = BookService.update_book(book_id, data['title'], data['author'], data['price'])

    if not updated_book:
      return response_model(404, message='Erro ao atualizar livro', error='Livro não encontrado')

    return response_model(200, message='Livro atualizado com sucesso', data=updated_book.to_dict())

  except Exception as e:
    return response_model(400, message='Erro ao atualizar livro', error=str(e))


@book_controller.route('/api/books/delete/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
  try:
    deleted_book = BookService.delete_book(book_id)

    if not deleted_book:
      return response_model(404, message='Erro ao deletar livro', error='Livro não encontrado')
    
    return response_model(200, message='Livro deletado com sucesso')
  
  except Exception as e:
    return response_model(400, message='Erro ao deletar livro', error=str(e))

