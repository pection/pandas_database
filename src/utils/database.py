# @size: pection
# @Date:   2021-01-28T15:00:55+07:00
# @Last modified by:   pection
# @Last modified time: 2021-01-29T09:58:48+07:00



from typing import List, Tuple

from utils.database_connection import DatabaseConnection

Furniture = Tuple[int, str, str, int, str, str, int]


# def read_csv_file() -> None:

def create_furniture_table() -> None:
    with DatabaseConnection('furniture_data.db') as connection:
        cursor = connection.cursor()
        # SQLite automatically makes `integer primary key` row auto-incrementing (see link in further reading)
        cursor.execute(
        'CREATE TABLE furniture(id integer primary key, name text, size text, price integer, image text, link text, read integer default 0)')


def get_all_furniture() -> List[Furniture]:
    with DatabaseConnection('furniture_data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM furniture')
        furniture = cursor.fetchall()
    return furniture


def insert_book(name: str, size: str, price: int, image: str, link: str) -> None:
    with DatabaseConnection('furniture_data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(
            'INSERT INTO furniture (name, size, price, image, link ) VALUES (?, ?, ?, ?, ?)', (name, size, price, image,link))


def mark_book_as_read(name: str) -> None:
    with DatabaseConnection('furniture_data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE furniture SET read=1 WHERE name=?', (name,))


def delete_book(name: str) -> None:
    with DatabaseConnection('furniture_data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM furniture WHERE name=?', (name,))
