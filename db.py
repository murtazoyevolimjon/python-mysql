from colorama import Fore, Style
from mysql.connector.cursor import MySQLCursor


def create_books_table(cursor: MySQLCursor):
    """
    Create a 'books' table in the database if it doesn't exist.
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
 def create_books_table(cursor: MySQLCursor):
            available BOOLEAN NOT NULL
        );
    """)
    
def insert_book(cursor: MySQLCursor, title, author, published_year, genre, price, available):
    """
    Insert a new book into the 'books' table.
    """
    query = """
        INSERT INTO books (title, author, published_year, genre, price, available)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (title, author, published_year, genre, price, available))


def show_all_books(cursor: MySQLCursor):
    """
    Retrieve and display all books from the 'books' table.
    """
    cursor.execute("""
        SELECT * FROM books
    """)
    books = cursor.fetchall()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    for book in books:
        print(book)
        print(book)
def search_books_by_author_or_genre(cursor: MySQLCursor, search_type, search_value):
    """
    Search for books by author or genre.
    """
    query = f"SELECT id, {search_type} FROM books WHERE {search_type} = %s"
    cursor.execute(query, (search_value,))
    results = cursor.fetchall()
    for book in results:
        print(f"id: {book[0]}, {search_type}: {book[1]}")
def update_book_price(cursor: MySQLCursor, book_id, new_price):
    """
    Update the price of a specific book.
    """
    query = "UPDATE books SET price = %s WHERE id = %s"
    cursor.execute(query, (new_price, book_id))
    print(f"{Fore.GREEN}Kitob narxi muvaffaqiyatli yangilandi.{Style.RESET_ALL}")
def update_book_availability(cursor: MySQLCursor, book_id, available):
    """
    Update the availability of a specific book.
    """
    query = "UPDATE books SET available = %s WHERE id = %s"
    cursor.execute(query, (available, book_id))
    print(f"{Fore.GREEN}Kitob mavjudligi muvaffaqiyatli yangilandi.{Style.RESET_ALL}")
def delete_book(cursor: MySQLCursor, book_id: int):
    """
    Delete a specific book from the 'books' table.
    """
    query = "DELETE FROM books WHERE id = %s"
    cursor.execute(query, (book_id,))
    print(f"{Fore.GREEN}Kitob muvaffaqiyatli o'chirildi.{Style.RESET_ALL}")
def sort_books_by_year(cursor: MySQLCursor, order="ASC"):
    """
    Retrieve books sorted by published year.
    """
    query = f"SELECT * FROM books ORDER BY published_year {order}"
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        print(f"{Fore.YELLOW}Kitoblar {order} tartibda saralandi:{Style.RESET_ALL}")
        for book in results:
            print(book)
    else:
        print(f"{Fore.RED}Hech qanday kitob topilmadi.{Style.RESET_ALL}")
def count_books(cursor: MySQLCursor):
    """
    Count the total number of books in the 'books' table.
    """
    cursor.execute("SELECT COUNT(*) FROM books")
    count = cursor.fetchone()[0]
    print(f"{Fore.BLUE}Jami kitoblar soni: {count}{Style.RESET_ALL}")
def price_statistics(cursor: MySQLCursor):
    """
    Display min, max, and average price of books.
    """
    cursor.execute("SELECT MIN(price), MAX(price), AVG(price) FROM books")
    min_price, max_price, avg_price = cursor.fetchone()
    print(f"{Fore.BLUE}Min narx: {min_price}, Max narx: {max_price}, O'rtacha narx: {avg_price:.2f}{Style.RESET_ALL}")