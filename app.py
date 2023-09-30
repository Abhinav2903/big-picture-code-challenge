from flask import Flask, render_template, jsonify, request
# Import the fetch_book_details function
from fetch_book import fetch_book_details

app = Flask(__name__)


def validate_isbn(isbn):
    # Remove any dashes or spaces
    isbn = isbn.replace("-", "").replace(" ", "")
    print("ISBN Replaced", isbn)
    # Check if the ISBN is 10 or 13 digits
    if len(isbn) not in [10, 13]:
        print("ISBN length", len(isbn))
        return False


# Validate ISBN-10
    if len(isbn) == 10:
        if not isbn[:-1].isdigit():
            return False
        total = 0
        for i in range(9):
            # for each character, multiply by a different decreasing number: 10 - x
            total = total + int(isbn[i]) * (10 - i)

     # Handle last character
        if isbn[9].lower() == "x":
            total += 10
        else:
            total += int(isbn[9])

        print(total)  # For debugging if required

    # Return whether the isbn is valid
        if total % 11 == 0:
            return True
        else:
            return False

    # Validate ISBN-13
    if len(isbn) == 13:
        if not isbn.isdigit():
            return False

        total = sum(int(digit) * (1 if i % 2 == 0 else 3)
                    for i, digit in enumerate(isbn[:-1]))
        checksum = int(isbn[-1])

        return (10 - (total % 10)) % 10 == checksum

    return False

# This route handles the book details by ISBN


@app.route("/isbn/", methods=['GET'])
def search_by_isbn():
    # Handle the search logic here based on the provided ISBN
    # access the ISBN using request.args.get('isbn')
    search_isbn = request.args.get('isbn')
    print("ISBN", search_isbn)

    if not validate_isbn(search_isbn):
        get_book_response = "Invalid ISBN format."
        return render_template('home.html', isbn=search_isbn, book_details={"error": get_book_response}), 400

    # logic to fetch book details based on the ISBN
    else:
        book_details = fetch_book_details(search_isbn)
        print(book_details)
    return render_template('home.html', isbn=search_isbn, book_details=book_details)


# This route handles the homepage with the search form
@app.route("/", methods=['GET'])
def home():
    return render_template('home.html', isbn="")


if __name__ == "__main__":
    app.run(debug=True)
