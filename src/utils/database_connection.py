# @Author: Naphat Nithisopa <pection>
# @Date:   2020-12-29T11:34:23+07:00
# @Email:  pection.naphat@gmail.com
# @Last modified by:   pection
# @Last modified time: 2021-01-29T09:21:58+07:00
import sqlite3


class DatabaseConnection:
    def __init__(self, host: str):
        self.connection = None
        self.host = host

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
