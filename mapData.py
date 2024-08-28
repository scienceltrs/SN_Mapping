import pandas as pd 
import csv
from pathNames import rawDataPath, autoOutputPath

data = pd.read_csv(rawDataPath, encoding='latin1')

data["LT Service Category"] = ""

data.sort_values(['Incident #'],axis = 0, inplace = True)
i = 0
for index, row in data.iterrows(): 
    # Possible conditions to check #
    type = row["Type"]
    service = row["Service (u_service)"]
    offering = row["Offering"]
    item = row["Item"]
    email = row["Preferred Email"]
    shortDescrip = row["Short description"]
    shortDescrip_lower = shortDescrip.lower()
    processSubstrings = {
        "SD",
        "LT Hub Service Request - ",
        "Add instructor",
        "remove student",
        "LT Hub Popup - ",
        "roster sync",
        "sync roster",
        "account"
    }
    quizSubstrings = {
        "quiz"
    }
    # Mapped Results #
    if item in ['Quizzes', 'Grades', 'Assignments']:
        data.at[index, "LT Service Category"] = "Assessment"
        continue
    if offering in ["Kaltura"] or item in ["Files", "Announcements"]:
        data.at[index, "LT Service Category"] = "Content Delivery"
        continue
    if type in ["Password"] or email in ["noreply@google.com", "no-reply@accounts.google.com"] or offering in ["Adapter", "Offboarding"]:
        data.at[index, "LT Service Category"] = "N/A"
        continue
    if ("Course Team Request") in shortDescrip:
        data.at[index, "LT Service Category"] = "Process"
        continue

    if item in ['User Enrolment Management', "Section Management","Standing Deferred Access", "Course Copies", "Admin Access", "Setup", "Course Management", "Settings","User Account","Integrations"]:
        data.at[index, "LT Service Category"] = "Process"
        continue
    else:
        if any(substring.lower() in shortDescrip_lower for substring in processSubstrings):
            data.at[index, "LT Service Category"] = "Process"
            i+=1 #for testing purposes
            continue
            
        if ("add") in shortDescrip_lower and pd.isna(item):
            data.at[index, "LT Service Category"] = "Process"
            continue
        if ("access") in shortDescrip_lower and item not in ["Files"]:
            data.at[index, "LT Service Category"] = "Process"
            continue
    if any(substring.lower() in shortDescrip_lower for substring in quizSubstrings):
        data.at[index, "LT Service Category"] = "Assessment"
           
print(i) #for testing purposes
#Copy result to output file#        
data.to_csv(autoOutputPath, index = False)