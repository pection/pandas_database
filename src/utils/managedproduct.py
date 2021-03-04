# @Author: Naphat Nithisopa <pection>
# @Date:   2020-12-29T11:34:23+07:00
# @Email:  pection.naphat@gmail.com
# @Last modified by:   pection
# @Last modified time: 2021-01-29T09:21:58+07:00
import pandas as pd


class ManageProductCode:

    def __init__(self, filepath: str):
        self.file_path = filepath
        index_csv = filepath.index("csv")

        self.product_code = filepath[index_csv - 3:index_csv - 1]
        self.values = 0
        self.columns_name = [
            "Product_Name",
            "Product_Size",
            "Prodcut_Prize",
            "Product_Image",
            "Product_Link",
        ]

    def read_csv_file(self):
        df = pd.read_csv(self.file_path, names=self.columns_name)
        self.values = df.shape[0]
        print("Check row success")

    def get_product_details(self):
        print("Your path is " + self.file_path)
        print("Your product code is " + self.product_code)
