# @Author: Naphat Nithisopa <pection>
# @Date:   2021-01-08T22:19:48+07:00
# @Email:  pection.naphat@gmail.com
# @Filename: app.py
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
        print(f'File path is a {jsonpath[0]}')
        return jsonpath[0]
        # return path
    except OSError as e: 
        path = [os.path.abspath(x) for x in os.listdir(os.getcwd())]
        jsonpath = [i for i in (list(map(lambda x: x if ".json" in x else None,path))) if i]
        print(f'File path is a {jsonpath[0]}')
        return jsonpath[0]
        print(f'Oops!  That was no valid path.  Try again...')
if __name__ == '__main__':
    instanceNames=["DT","SF","BE","CT","WD","ST","LC","NT","DC","TS"]
    file_path_json=get_file_path()
    try:
        file_json =open(file_path_json,)
        path_file = json.load(file_json)
        file_json.close()
    except ValueError:
        print(f'{file_path_json} not found')
    # zipfile = zip(instanceNames,file_path)
    # dict_zip = dict(zipfile)
    # holder = {name: ManageProductCode(name=name) for name in instanceNames}
    Dining_table = ManageProductCode(path_file[instanceNames[0]])
    Sofa = ManageProductCode(path_file[instanceNames[1]])
    Bed = ManageProductCode(path_file[instanceNames[2]])
    Coffe_table = ManageProductCode(path_file[instanceNames[3]])
    Working_desk = ManageProductCode(path_file[instanceNames[4]])
    Side_table = ManageProductCode(path_file[instanceNames[5]])
    Living_room_Cabinet = ManageProductCode(path_file[instanceNames[6]])
    Negotiating_table = ManageProductCode(path_file[instanceNames[7]])
    Dining_chair = ManageProductCode(path_file[instanceNames[8]])
    Tv_stand = ManageProductCode(path_file[instanceNames[9]])
    
    Dining_table.read_csv_file()
    Dining_table.get_product_details()
    
    breakpoint()
    # Dining_table.remove_link_string()
    
    
    
    # Working_dest.add_product_code()
    # Working_dest.update_csv_file()