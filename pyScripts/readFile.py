#Note : The written functions need to be executed one by one at a time
import pandas as pd 
from bs4 import BeautifulSoup
import json
from operator import itemgetter


def extractAddressPhone(frame):
    for each in frame:
        if(str(each)=="nan"):
            
            break
        if "Address:" in each:
            valid_objects_address.append(each)
        elif "Phone:" in each:
            valid_objects_phone.append(each)
    
    for i in range(0,len(valid_objects_address)):
        soupAddress=BeautifulSoup(valid_objects_address[i],'html.parser')
        soupPhone=BeautifulSoup(valid_objects_phone[i],'html.parser')
        
        obj={
            "Address":soupAddress.p.text.replace(" ",'').split('\n')[2],
            "Phone":soupPhone.p.text.replace(" ",'').split('\n')[2]
        }
        array_of_objects.append(obj)
    
    with open('../logs/resut.json','w') as f:
        f.write(json.dumps(array_of_objects))
    print("Done")


def extractName(frame):
    arrayNames=[]
    for each in frame:
        if(str(each)=="nan"):
            break
        soupName=BeautifulSoup(each,'html.parser')
        arrayNames.append(soupName.h2.text)
    
    arrayNames=arrayNames[:len(arrayNames)-3]
    

    with open('../logs/resut.json','r') as f:
        objects=json.loads(f.read())
    i=0
    for each in objects:
        each["Name"]=arrayNames[i]
        i+=1

    
    with open('../logs/resut.json','w') as f:
        f.write(json.dumps(objects))
    print("Done")



def extractSite_Description(frame):
    with open('../logs/resut.json','r') as f:
        objects=json.loads(f.read())
    
    foundAddress = list(map(itemgetter('Address'), objects))
    
    framePointer=0
    foundPointer=0
    indexes=[]
                
    while(foundPointer<len(foundAddress) and framePointer<len(frame)):
        copyFrame=frame[framePointer]  # This is to remove spaces as it matches with the Address in JSON object
        if copyFrame.replace(' ','')==foundAddress[foundPointer]:
            indexes.append(framePointer)
            foundPointer+=1
        framePointer+=1
    
    print(indexes)
    
    updating_objects=[]

    for i in range(0,len(indexes)-1):
        count=indexes[i+1]-indexes[i]
        if count>1:
            obj={
                "Address":frame[indexes[i]],
                "Site":frame[indexes[i]+1],
                "Description":frame[indexes[i]+2]
            }
        else:
            obj={
                "Address":frame[indexes[i]],
                "Site":frame[indexes[i]+1],
            }
        updating_objects.append(obj)
    
    final_obj={
        "Address":frame[indexes[-1]],
        "Site":frame[indexes[-1]+1],
        "Description":frame[indexes[-1]+2]
    }

    updating_objects.append(final_obj)

    i=0
    
    for each in objects:
        each['Address']=updating_objects[i]["Address"]
        each['Site']=updating_objects[i]['Site']
        each['Description']=updating_objects[i]['Description']
        i=i+1
    
    with open('../logs/resut.json','w') as f:
        f.write(json.dumps(objects))
    print("Done")





if __name__=="__main__":
    FILE="../FILES/csv/result (1).csv"
    df=pd.read_csv(FILE,delimiter=',')
    
    #print(df['Address'])
    valid_objects_address=[]
    valid_objects_phone=[]

    array_of_objects=[]
    #extractAddressPhone(df['Phone'])  #Uncomment to read Address and Phones
    #extractName(df['Name'])           #Uncomment to read Name  
    #extractSite_Description(df['Address']) #Uncomment to update json with Site and Description
    