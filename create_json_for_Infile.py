#project: None
#Module: Inbound File Processing
#Description: Create a Json File for Input File
#Date: 18/11/2020
#Author: Naveen
#----------------------------------------------------------------------------------------------------------------------#
import csv
import json
#path='C:/Users/NAVEEN/Desktop/'
path=input("Enter path:")
#input_file = 'ASTRAZEN_DIPRIVAN_ACCREDO_DISPENSE_11112020.txt'
input_file=input("Input_file_Name:")
s=input_file.split('.')
json_file = 'school3.json'

def read_CSV(path,input_file, json_file):
    rows = []
    f=[]
    with open(path+input_file) as csvfile:
        reader = csv.reader(csvfile,delimiter='|')
        #print(csvfile)
        for row in reader:
            rows.append(row)
    rows.pop(0)
    h=rows[0]
    #print((h))
    m=[i for  i in rows[1:]]
    for j in range(0,len(m)):
       z=zip(h,m[j])
       d=dict(z)
       f.append(d)
    convert_write_json(f, path+s[0]+".json")
def convert_write_json(data, json_file):
    with open(json_file, "w") as f:
        f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '))) #for pretty
        #f.write(json.dumps(data))
read_CSV(path,input_file,json_file)