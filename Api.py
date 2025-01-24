from flask import Flask ,jsonify ,request

app = Flask(__name__)

books = [{"id":1,"title":"The Great Gatsby ","author": "F.Scott "},
         {"id": 2,"title":"To Kill a Mockingbird ", "author":"Harper Lee "},
        {"id": 3,"title": "1984","author":"George Orwell "}]

@app.route("/")
def home():
    return "Home of book api made with love  "

@app.route('/books',methods =['GET'])
def get_books():
    return jsonify(books), 200

@app.route('/books/<int:id>',methods = ['GET'])
def get_book_by_id (id):
    book = next((book for book in books if book ['id'] == id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "book not found "}),  404

@app.route("/books/author/<string:author>", methods=['GET'])
def get_books_by_author(author):
    author_books= [book for book in books if book['author'].strip().lower() == author.strip().lower()]
    if author_books:
        return jsonify(author_books)
    return jsonify({"error":" No book found for this autho"}),404

@app.route('/books', methods =['POST'])
def add_book():
    new_book = request.get_json()
    if "title" in new_book and "author" in new_book :
        new_book['id'] = max(book['id'] for book in books ) +1 if books else 1
        books.append(new_book)
        return jsonify(new_book), 201
    return jsonify({"error":"Invalid book data"}), 400


if __name__== '__main__':
    app.run(debug=True)

