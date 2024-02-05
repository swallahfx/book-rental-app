import requests

def fetch_book_details(title):
    """
    Fetch book details from OpenLibrary API based on the title.
    Extract the number_of_pages or number_of_pages_median attribute.
    """
    api_url = f'https://openlibrary.org/search.json?title={title}'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        docs = data.get('docs', [])

        if docs:
            book_info = docs[0]
            number_of_pages = book_info.get('number_of_pages')
            number_of_pages_median = book_info.get('number_of_pages_median')

            if number_of_pages:
                return number_of_pages
            elif number_of_pages_median:
                return number_of_pages_median

    return None
