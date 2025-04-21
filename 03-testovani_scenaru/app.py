from flask import Flask, render_template, jsonify, abort

app = Flask(__name__)

# Ukázková data knih
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
]

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/api/books')
def api_books():
    return jsonify(books)

@app.route('/api/books/<int:book_id>')
def api_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    abort(404)

@app.route('/home')
def homepage():
    return render_template('home.html')

@app.route('/api/author')
def api_author():
    return jsonify({'author': 'John Doe'})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
