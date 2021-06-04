import pandas as pd
import sys
import os
import cProfile
def save_data(json_data):
    '''
    Desc:  saves the merged data to csv files
    args: 
        json_data:(DICT) contains dictionary with csv names and values as combined data
    return: False
    '''
    mapping={"detail.csv":"Detail_67_","detailVol.csv":"DetailVol_67_","detailTemp.csv":"DetailTemp_67_"}
    for i in json_data:
        if i!= "columns":
            df=pd.DataFrame(json_data[i],columns=json_data["columns"][mapping[i]])
            print("Saving file...",i)
            df.to_csv(i,index=False)

            
def get_json_data(file_names):
    '''
    Desc:  Combines data from different files
    args: 
        file_names:(LIST) contains file names to be merged
    return: Json data containing indivisual file names and data
    '''
    poi=["Detail_67_","DetailVol_67_","DetailTemp_67_"]
    save_file={"detail.csv":[],"detailVol.csv":[],"detailTemp.csv":[],"columns":{}}
    for file in file_names:
        excel=pd.ExcelFile(file)
        sheet_names=excel.sheet_names
        for sheet in sheet_names:
            print("Parseing:",sheet)
            if sheet.startswith("Detail_67_"):
                data=excel.parse(sheet)
                save_file["detail.csv"].extend(data.values)
                if "Detail_67_" not in save_file["columns"]:
                    save_file["columns"]["Detail_67_"]=data.columns
            elif sheet.startswith("DetailVol_67_"):
                data=excel.parse(sheet)
                save_file["detailVol.csv"].extend(data.values)
                if "DetailVol_67_" not in save_file["columns"]:
                    save_file["columns"]["DetailVol_67_"]=data.columns
            elif sheet.startswith("DetailTemp_67_"):
                data=excel.parse(sheet)
                save_file["detailTemp.csv"].extend(data.values)
                if "DetailTemp_67_" not in save_file["columns"]:
                    save_file["columns"]["DetailTemp_67_"]=data.columns
    return save_file
def runner(filenames):
    data_json=get_json_data(file_names)
    save_data(json_data=data_json)
if __name__=='__main__':
    #print(sys.argv)
    if len(sys.argv)>1:
        #data_1="data.xlsx"
        #data_2="data_1.xlsx"
        file_names=[sys.argv[1],sys.argv[2]]
        for file in file_names:
            if not os.path.exists(file):
                print(file+" No such file!!!")
                sys.exit(0)
        data_json=get_json_data(file_names)
        save_data(json_data=data_json)
    else:
        data_1="data.xlsx"
        data_2="data_1.xlsx"
        file_names=[data_1,data_2]
        for file in file_names:
            if not os.path.exists(file):
                print(file+" No such file!!!")
                sys.exit(0)
        runner(file_names)
        #cProfile.run('runner(file_names)')
        
        
           
        
    
        
        