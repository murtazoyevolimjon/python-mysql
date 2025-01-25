from colorama import Fore, Style
import mysql.connector
import settings
from db import (
    create_books_table,
    insert_book,
    show_all_books,
    search_books_by_author_or_genre,
    update_book_price,
    update_book_availability,
    delete_book,
    sort_books_by_year,
    count_books,
    price_statistics
)

if __name__ == "__main__":
    try:
        connection = mysql.connector.connect(
            host=settings.host,
            user=settings.user,
            password=settings.password,
            port=settings.port
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {settings.db_name}")
        cursor.execute(f"USE {settings.db_name}")
        create_books_table(cursor)
        connection.commit()

        while True:
            print(f"{Fore.LIGHTCYAN_EX} == Kutubxona tabeli == {Fore.RESET}")
            print(f"\n{Fore.LIGHTCYAN_EX}1 --> Yangi kitob qo'shish {Fore.RESET}")
            print(f"{Fore.LIGHTCYAN_EX}2 --> Barcha kitoblar ruyxatini ko'rish {Fore.RESET}")
            # Boshqa menyu qismlari...

            choice_menu = int(input(f"{Fore.LIGHTGREEN_EX}Xizmat turini tanlang {Fore.RESET} "))
            if choice_menu == 1:
                length = int(input(f"{Fore.LIGHTYELLOW_EX}Nechta kitob qo'shmoqchisiz {Fore.RESET} "))
                for i in range(length):
                    available_input = input(f"{Fore.LIGHTRED_EX}Mavjudmi (Ha yoki Yo'q): {Fore.RESET} ").strip().lower()
                    available = True if available_input == "ha" else False
                    insert_book(
                        cursor,
                        title=input("Kitob nomi: "),
                        author=input("Muallif: "),
                        published_year=int(input("Nashr yili: ")),
                        genre=input("Janr: "),
                        price=float(input("Narxi: ")),
                        available=available
                    )
                    print(f"{Fore.BLUE}Kitob muvaffaqiyatli qo'shildi!{Fore.RESET}")
                    connection.commit()
            elif choice_menu == 2:
                show_all_books(cursor)
            elif choice_menu == 10:
                print(f"{Fore.BLUE}Dasturdan chiqildi {Fore.RESET}")
                break
            else:
                print(f"{Fore.RED}Noto'g'ri xizmat turi tanlandi!{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}Xato yuz berdi: {e}{Style.RESET_ALL}")
    finally:
        cursor.close()
        connection.close()
