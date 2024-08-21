import pandas as pd 
import csv
from pathNames import rawDataPath, autoOutputPath

data = pd.read_csv(rawDataPath, encoding='ISO-8859-1')

data["LT Service Category"] = ""

data.sort_values(['Incident #'],axis = 0, inplace = True)

for index, row in data.iterrows(): 
    item = row["Item"]
    service = row["Service (u_service)"]
    offering = row["Offering"]
    #if item type is SD, course copies or user enrolment -> Process
    if item in ['User Enrolment Management', "Section Management","Standing Deferred Access", "Course Copies", "Admin Access"]:
        data.at[index, "LT Service Category"] = "Process"
    if service in ["Email Services"]:
        data.at[index, "LT Service Category"] = "N/A"
    if item in ['Quizzes']:
        data.at[index, "LT Service Category"] = "Assessment"
    if offering in ["Kaltura"]:
        data.at[index, "LT Service Category"] = "Content Delivery"
data.to_csv(autoOutputPath, index = False)