from flask import Flask,render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from fetch_book import get_book_details, validate_isbn

#Flask App initialization 
app = Flask(__name__)

#Flask Database Configuration can also be done by config file 
#the username and password can be masked into the enviornment varaible for security reasons
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:abhi2903@127.0.0.1:3306/flaskdatabase?charset=utf8mb4'
db = SQLAlchemy(app)

# import model from the Library
from models import Library


@app.route("/isbn/", methods=['GET'])
def search_by_isbn():
    # access the ISBN using request.args.get('isbn')
    search_isbn = request.args.get('isbn')

    if not validate_isbn(search_isbn):
        get_book_response = "Invalid ISBN format."
        return render_template('home.html', isbn=search_isbn, book_details={"error": get_book_response}), 400

    # fetch book details based on the ISBN
    else:
        book_details = get_book_details(search_isbn)
    return render_template('home.html', isbn=search_isbn, book_details=book_details)

# This route handles the homepage with the search form
@app.route("/", methods=['GET'])
def home():
    return render_template('home.html', isbn="")


# This route handles the books api call that handle adding and retriving books to the library 
@app.route('/books', methods=['GET', 'POST'])
def create_book():

    if request.method == "GET":
        books = Library.query.all()
        # Convert the books to a list of JSON objects
        books_json = [book.to_json() for book in books]
        return render_template('displayBooks.html', books=books_json)
    
    if not request.json:
        return 400

    book = Library(
        isbn=request.json.get('isbn'),
        title=request.json.get('title'),
        author=request.json.get('author'),
        cover=request.json.get('cover'),
        summary=request.json.get('summary')
    )
    # commit and add the books to the database
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_json()), 201
