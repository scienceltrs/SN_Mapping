import pandas as pd 
import csv
from pathNames import rawDataPath, autoOutputPath

######################
#### DO NOT EDIT ####
######################
def checkSubstring(a,b):
    return any(x.lower() in b for x in a)

def checkExactSubstring(a,b):
    return any(x.lower() in b.split() for x in a)

data = pd.read_csv(rawDataPath, encoding='latin1')

data["LT Service Category"] = ""

i = 0   # for testing purposes
j = 0   # for testing purposes
k = 0   # for testing purposes



for index, row in data.iterrows(): 
    # Possible conditions to check #
    type                = row["Type"]
    service             = row["Service (u_service)"]
    offering            = row["Offering"]
    item                = row["Item"]
    email               = row["Preferred Email"]
    shortDescrip        = row["Short description"]
    shortDescrip_lower  = shortDescrip.lower()


    ############################
    #### START EDITING HERE ####
    ############################
    processSubstrings   = {
        "SD",
        "LT Hub Service Request - ",
        "Add instructor",
        "remove student",
        "LT Hub Popup - ",
        "roster sync",
        "sync roster",
        "account",
        "import",
        "copy",
        "roster",
        "create",
        "integration",
        "setup",
        "sync",
        "set up",
        "setting",
        "creating",
        "duplicat", #captures both duplicate + duplicating
    }
    quizSubstrings          = {
        "quiz"
    }
    naSubstrings            = {
        "receipt"
    }
    assessmentExactSubtring = {
        "grade",
        "grades",
        "gradebook"
    }
    processItems            = {
        'User Enrolment Management', 
        "Section Management",
        "Standing Deferred Access",
        "Course Copies", 
        "Admin Access", 
        "Setup", 
        "Course Management", 
        "Settings",
        "User Account",
        "Integrations"
        
    }
    assessmentItems        = {
        'Quizzes', 
        'Grades', 
        'Assignments'
    }
    naOfferings            = {
        "Adapter", 
        "Offboarding", 
        "Not Listed"
    }

    # Mapped Results #
    if item in processItems:
        data.at[index, "LT Service Category"] = "Process"
        continue

    else:
        if checkSubstring(processSubstrings, shortDescrip_lower):
            data.at[index, "LT Service Category"] = "Process"
            #print(shortDescrip_lower) #for testing purposes
            j+=1 #for testing purposes
            continue
            
        if (checkSubstring(["add"], shortDescrip_lower) and pd.isna(item)):
            data.at[index, "LT Service Category"] = "Process"
            continue

        if (checkSubstring(["access"], shortDescrip_lower)and item not in ["Files"]):
            data.at[index, "LT Service Category"] = "Process"
            print(shortDescrip_lower)
            continue 

    if item in assessmentItems:
        data.at[index, "LT Service Category"] = "Assessment"
        continue

    if offering in ["Kaltura"] or item in ["Files", "Announcements"]:
        data.at[index, "LT Service Category"] = "Content Delivery"
        continue

    if type in ["Password"] or email in ["noreply@google.com", "no-reply@accounts.google.com"] or offering in naOfferings or checkSubstring(naSubstrings,shortDescrip_lower):
        data.at[index, "LT Service Category"] = "N/A"
        continue
    
    if ("Course Team Request") in shortDescrip:
        data.at[index, "LT Service Category"] = "Process"
        continue

    if checkSubstring(quizSubstrings,shortDescrip_lower): 
        data.at[index, "LT Service Category"] = "Assessment"
        continue

    if (checkExactSubstring(assessmentExactSubtring,shortDescrip_lower) and checkSubstring(["sync"],shortDescrip_lower)):
        data.at[index, "LT Service Category"] = "Assessment"
        continue    


print("this is j:", j) #for testing purposes
print("this is i:", i) #for testing purposes
print("this is k:", k) #for testing purposes


######################
#### DO NOT EDIT ####
######################
#Copy result to output file#        
data.to_csv(autoOutputPath, index = False)