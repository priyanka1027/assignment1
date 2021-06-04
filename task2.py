import pandas as pd
import sys
import os
import cProfile


def save_downsample(df,name):
    
    '''
    Desc:  saves downsampled files
    args: 
        df:(pandas dataFrame) contains downsampled data
        name: (str) filename
    return: False
    '''
    print("Saving file...",name)
    df.to_csv(name,index=False)
def downsample(df,lag=60):
    '''
    Desc:  Downsamples data at lag 
    args: 
        df:(pandas dataFrame) contains downsampled data
        lag: (int) lag timing
    return: downsampled data
    '''
    final_data=[]
    for lag_range in range(0,len(df),lag):
        final_data.append(df.iloc[lag_range].values)
    return pd.DataFrame(final_data,columns=df.columns)
def runner():
    mapping={"detail.csv":"detailDownsampled.csv","detailTemp.csv":"detailVolDownsampled.csv","detailVol.csv":"detailTempDownsampled.csv"}
    for file in mapping:
        df=pd.read_csv(file)
        ndf=downsample(df)
        save_downsample(ndf,mapping[file])

if __name__=='__main__':
    runner()
    #cProfile.run('runner()')