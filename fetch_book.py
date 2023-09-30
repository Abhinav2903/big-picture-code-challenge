import requests  # Import the 'requests' library

def fetch_book_details(isbn):
    base_url = "https://openlibrary.org/api/books"
    params = {
        "bibkeys": f"ISBN:{isbn}",
        "format": "json",
        "jscmd": "details"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        book_data = response.json().get(f"ISBN:{isbn}", {})
        # print("Book Data",book_data)
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
