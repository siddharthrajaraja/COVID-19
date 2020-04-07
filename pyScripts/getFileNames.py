import os
import time
import json
import datetime
from operator import itemgetter
# This function gets names of all csv files provided to maintain a log in backend which files are present in backend.
def getAllCsv():
        
    for root,dirs,files in os.walk('../FILES/csv',topdown=False):
        for file in files:
            print(file)
            obj={
                    'name':file,
                    'status':0,
                    'timestamp':str(datetime.datetime.now())
            }        

            with open('../logs/csv_files.json','r') as f1:
                array=json.load(f1)
                
                found = list(map(itemgetter('name'), array))
                if obj['name'] not in found:
                    array.append(obj)
                    print(array)
                    with open('../logs/csv_files.json','w') as f2:
                        json.dump(array,f2)
                
                
# This is for xlsx files when it will be provided 
def getAllXlsx():
    for root,dirs,files in os.walk('../FILES/xlsx',topdown=False):
        print(files)

if __name__=="__main__":
    getAllCsv()