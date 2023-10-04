import requests  # Import the 'requests' library
# Handle the search logic here based on the provided ISBN
def validate_isbn(isbn):
    # Remove any dashes or spaces
    isbn = isbn.replace("-", "").replace(" ", "")
    # Check if the ISBN is 10 or 13 digits
    if len(isbn) not in [10, 13]:
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

#fetch book details logic
def get_book_details(isbn):
    # fetch book from the third party api
    base_url = "https://openlibrary.org/api/books"
    params = {
        "bibkeys": f"ISBN:{isbn}",
        "format": "json",
        "jscmd": "details"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # fetch all the required values from the json received and also set defualt values if not found
        book_data = response.json().get(f"ISBN:{isbn}", {})
        title = str(book_data.get("details", {}).get("title", "Title not available"))
        authors = [str(book_data.get("details").get("authors")[0].get('name'))]
        cover_url = book_data.get('thumbnail_url', 'Cover URL not available')
        summary = book_data.get('details', {}).get('description', 'Summary not available')

        # Create a dictionary to store the extracted data
        book_details = [{
        "title": title,
        "authors": ", ".join(authors),
        "cover":cover_url,
        "summary":summary
        }]
        return book_details
    else:
        print(f"Failed to fetch book details for ISBN {isbn}")
        return None
