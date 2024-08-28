## Biblioseek Project

# Biblioseek

## Description

Biblioseek, the Library Management System is a Python project utilizing Tkinter and PIL libraries. This project is a web-based application that allows users to log in, search for books, view book details, and provide feedback for books they have read. Users can search for books by entering the book name and author, and the system will display information about the book if it is present in the database. If the book is not found, a message indicating its absence will be shown.

The system also includes a feedback feature, where users can view feedback provided by previous readers for a particular book. Users can also submit their own feedback after reading a book, which will be stored in the system and made available for others to view as recommendations.
## Features

- User authentication
- Book search by title and author
- Detailed book information display
- Feedback and recommendation system
- User registration and account management
- Admin panel for library staff to manage books, users, and feedback.




## Tech Stack

- Python 3.x
- Tkinter
- PIL (Python Imaging Library)
- MySQL(database)
- Latex(ppt)

## Installation

Install dependencies

1. Clone the repository:

    bash
    git clone https://github.com/anvika6677/BIBLIOSEEK.git
    

2. Install dependencies:

    pip install tkinter,pillow
    pip install mysql-connector-python
    python.exe -m pip install --upgrade pip -


    

3. Run the application:

    python main_file.py
    
    
## Usage

- Launch the application by running main.py.
- Log in with your credentials 
- Use the search feature to find books by entering the book title and/or author.
- View detailed information about each book, including availability and location.
- Leave/ view feedback and recommendations for books you've read to contribute to the community.


## Example

### Searching for a Book

To search for a book by title and author, use the following command:

python first_window.py --search "The Great Gatsby" --author "F. Scott Fitzgerald"