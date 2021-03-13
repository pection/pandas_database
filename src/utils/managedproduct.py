# @Author: Naphat Nithisopa <pection>
# @Date:   2020-12-29T11:34:23+07:00
# @Email:  pection.naphat@gmail.com
# @Last modified by:   pection
# @Last modified time: 2021-01-29T09:21:58+07:00
import pandas as pd
from typing import List, Tuple


class ManageProductCode:
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    def __init__(self, filepath: str):
        self.file_path = filepath
        self.values = 0
        self.columns_name = [
            "Product_Name",
            "Product_Size",
            "Prodcut_Prize",
            "Product_Image",
            "Product_Link",
        ]

    def read_csv_file(self):
        index_csv = self.file_path.index("csv")

        self.product_code = self.file_path[index_csv - 3:index_csv - 1]
        self.df = pd.read_csv(self.file_path, names=self.columns_name)
        self.values = self.df.shape[0]+1

        print(f'Read csv file and convert to DataFrame successfully')

    def get_product_details(self):
        print(f'Your path is {self.file_path}')
        print(f'Your product code is {self.product_code}')
        print(f'Your CSV file have {self.values} row')    
        return [self.file_path ,self.product_code]
    
    def add_product_code(self):
        
        product_id = [self.product_code+"-"+str(i) for i in range(1,self.values)]
        self.df['Product_ID'] = product_id 

        print(f'Add {self.values} product id with {self.product_code} ')

    def create_furniture_table(self) -> None:
        with DatabaseConnection('furniture_data.db') as connection:
            cursor = connection.cursor()
            # SQLite automatically makes `integer primary key` row auto-incrementing (see link in further reading)
            cursor.execute(
            'CREATE TABLE IF NOT EXISTS furniture(id integer primary key, name text, size text, price integer, image text, link text, code text, read integer default 0)')
        
    def get_all_furniture(self) -> List[Furniture]:
        with DatabaseConnection('furniture_data.db') as connection:
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM furniture')
            furniture = cursor.fetchall()
        return furniture
    def delete_furniture(product_code: str) -> None:
        with DatabaseConnection('furniture_data.db') as connection:
            cursor = connection.cursor()

            cursor.execute('DELETE FROM furniture WHERE code=?', (product_code,))

    def insert_furniture(self,dataframe) -> None:
        with DatabaseConnection('furniture_data.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO furniture (name, size, price, image, link, code) VALUES (?, ?, ?, ?, ?, ?)', (self.df["Product_Name"], self.df["Product_Size"], self.df["Product_Prize"], self.df["Product_Image"],self.df["Product_link"],self.df["Product_ID"]))
    