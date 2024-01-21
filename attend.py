import pandas as pd
import os
from datetime import date
import openpyxl
import numpy as np
global date
date =str(date.today().strftime("%d/%m/%Y"))
def add(name,regno):
    if os.path.isfile("Attendence.xlsx") ==False:
        stud_list={"NAME":[],"RegNO":[],date:[]}
        df=pd.DataFrame(data=stud_list)
        df.to_excel("Attendence.xlsx",index=False)
    Student={"Name":[str(name)],"RegNO":[str(regno)],date:[""]}
    df_stud = pd.DataFrame(data=Student)
    df_stud = df_stud.astype("string")
    with pd.ExcelWriter('Attendence.xlsx', mode="a", if_sheet_exists="overlay") as writer:
        df_stud.to_excel(writer, startrow=writer.sheets["Sheet1"].max_row, header=False, index=False)

def attended(regno):
    df=pd.read_excel('Attendence.xlsx')
    df.loc[cls.df["REGNO"] == regno, date] = "P"
    df.to_excel(cls.database_file, index=False)
    
def display(regno): 
    student_data = df[cls.df["REGNO"] == regno]
    return student_data