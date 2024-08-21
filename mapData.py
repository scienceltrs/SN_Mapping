import pandas as pd 
import csv
from pathNames import rawDataPath, autoOutputPath

data = pd.read_csv(rawDataPath, encoding='latin1')

data["LT Service Category"] = ""

data.sort_values(['Incident #'],axis = 0, inplace = True)

for index, row in data.iterrows(): 
    # Possible conditions to check #
    type = row["Type"]
    service = row["Service (u_service)"]
    offering = row["Offering"]
    item = row["Item"]

    # Mapped Results #
    if item in ['User Enrolment Management', "Section Management","Standing Deferred Access", "Course Copies", "Admin Access"]:
        data.at[index, "LT Service Category"] = "Process"
    if item in ['Quizzes']:
        data.at[index, "LT Service Category"] = "Assessment"
    if offering in ["Kaltura"]:
        data.at[index, "LT Service Category"] = "Content Delivery"


#Copy result to output file#        
data.to_csv(autoOutputPath, index = False)