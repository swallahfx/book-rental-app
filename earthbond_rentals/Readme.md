### 1. Create and Activate a Virtual Environment
    *create**
    python3 -m venv venv

    **activate**
    windows : venv\Scripts\activate
    macos/linus: source venv/bin/activate

### Install Dependencies
  `pip install -r requirements.txt`

### Migrate Database

    `python3 manage.py makemigration`

    `python3 manage.py makemigration`

### Usage
    Run the DJANGO Server on your terminal:

    `ython3 manage.py runserver`

        The server will be available at http://127.0.0.1:8000, and you can change the port if needed.

    
    Here, you can test the  endpoints:
        use this link `http://127.0.0.1:8000/admin` to access the django-admin and manipulate the data as you want

    Endpoint 1: `http://127.0.0.1:8000/api/users/`  to create a user account(follow the prompt)
        Method: POST
        
    Endpoint 2: `http://127.0.0.1:8000/api/rentals/`
        Method: POST
        Description: Input all the requested data to rent a book
        Response: the price to pay for the renting period applicable to you then would be sent