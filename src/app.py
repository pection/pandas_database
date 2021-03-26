# @Author: Naphat Nithisopa <pection>
# @Date:   2021-01-08T22:19:48+07:00
# @Email:  pection.naphat@gmail.com
# @Filename: createpd.py
# @Last modified by:   pection
# @Last modified time: 2021-01-29T15:26:49+07:00


from utils.managedproduct import ManageProductCode
import pandas as pd
import os ,sys
# import numpy as np
import pdb 
import json

def get_file_path() -> str:
    try :
        os.chdir(os.getcwd()+"/dataset")
        path = [os.path.abspath(x) for x in os.listdir(os.getcwd())]
        jsonpath = [i for i in (list(map(lambda x: x if ".json" in x else None,path))) if i]
        return jsonpath[0]
        # return path
    except OSError as e: 
        print(f'Oops!  That was no valid path.  Try again...')
if __name__ == '__main__':
    print(os.chdir(os.path.dirname(os.path.abspath(__file__))))
    namecsv=["DT","SF","BE","CT","WD","ST","LC","NT","DC","TS"]
    file_path_json=get_file_path()
    try:
        file_json =open(file_path_json,)
        path_file = json.load(file_json)
        file_json.close()
    except ValueError:
        print(f'{file_path_json} not found')
    # zipfile = zip(namecsv,file_path)
    # dict_zip = dict(zipfile)
    Dining_table = ManageProductCode(path_file[namecsv[0]])
    Sofa = ManageProductCode(path_file[namecsv[1]])
    Bed = ManageProductCode(path_file[namecsv[2]])
    Coffe_table = ManageProductCode(path_file[namecsv[3]])
    Working_desk = ManageProductCode(path_file[namecsv[4]])
    Side_table = ManageProductCode(path_file[namecsv[5]])
    Living_room_Cabinet = ManageProductCode(path_file[namecsv[6]])
    Negotiating_table = ManageProductCode(path_file[namecsv[7]])
    Dining_chair = ManageProductCode(path_file[namecsv[8]])
    Tv_stand = ManageProductCode(path_file[namecsv[9]])
    
    Dining_table.read_csv_file()
    Dining_table.get_product_details()
    
    breakpoint()
    # Dining_table.remove_link_string()
    
    
    
    # Working_dest.add_product_code()
    # Working_dest.update_csv_file()