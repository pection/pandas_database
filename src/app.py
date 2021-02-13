# @Author: Naphat Nithisopa <pection>
# @Date:   2021-01-08T22:19:48+07:00
# @Email:  pection.naphat@gmail.com
# @Filename: createpd.py
# @Last modified by:   pection
# @Last modified time: 2021-01-29T15:26:49+07:00


# from utils import database
import pandas as pd
# import numpy as np
# import ipdb ; ipdb.set_trace()

if __name__ == '__main__':

    # product_code = filepath[index_csv - 3:index_csv - 1]

    columns_name = [
        "Product_Name",
        "Product_Size",
        "Prodcut_Prize",
        "Product_Image",
        "Product_Link",
        "Product_Code"
    ]

    dataset_path = '/home/pection/Backup/Program/pandas_database/src/dataset/Bed_dataset_BE.csv'

    df = pd.read_csv(dataset_path, names=columns_name)
    index_csv = dataset_path.index("csv")
    product_code = dataset_path[index_csv - 3:index_csv - 1]

    breakpoint()

    # os.chdir(os.getcwd()+"/dataset")
    # file_path = [os.path.abspath(x) for x in os.listdir(os.getcwd())]
    #
    # Working_dest = ManageProductCode(file_path[1])
    # Working_dest.get_product_details()
    # Working_dest.read_csv_file()
    # product_code_list= Working_dest.add_product_code()
    # print(product_code_list)
