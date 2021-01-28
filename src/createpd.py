# @Author: Naphat Nithisopa <Pection>
# @Date:   2020-12-29T19:37:40+07:00
# @Email:  pection.naphat@gmail.com
# @Project: MNFurniture
# @Filename: createpd.py
# @Last modified by:   Pection
# @Last modified time: 2020-12-30T13:15:37+07:00





import os
from utils import database


def menu():
    database.create_book_table()
if __name__ == '__main__':
    # os.chdir(os.getcwd()+"/dataset")
    #
    # file_path = [os.path.abspath(x) for x in os.listdir(os.getcwd())]
    #
    # Working_dest = ManageProductCode(file_path[1])
    # Working_dest.get_product_details()
    # Working_dest.read_csv_file()
    # product_code_list= Working_dest.add_product_code()
    # print(product_code_list)
    menu()
