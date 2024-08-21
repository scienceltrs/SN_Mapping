# ServiceNow Mapping Scripts
This repository contains a script to map tickets from ServiceNow into various LT Service Categories (Process, Assessment, Content Delivery, N/A).

# Getting Started
## Computer Setup
- Please have [VSCode](https://code.visualstudio.com/) and the [Python Extension](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites) installed
- Please have [Git](https://git-scm.com/downloads) installed
- Please have [Python](https://www.python.org/downloads/) installed
- Have the following packages installed: [Pandas](https://pypi.org/project/pandas/)

## Program Setup
1. [Clone this project](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
```
git clone https://github.com/scienceltrs/SN_Mapping.git
```
2. In SN_Mapping/input, add your raw data. Make sure that it's named: **data.csv**.

## Executing Program Using VSCode
1. Open mapData.py in VSCode then execute the script by pressing the arrow icon, "Run Python Script"
2. You can find the outputted file in SN_Mapping/output, titled: **outputData.csv**

## Next Steps
- Copy the file in the output file into an Excel Spreadsheet
- Filter by "(Blanks)" in the LT Service Category column and then manually complete accordingly

## Closing Remarks
While the script will not categorize all tickets, it will significantly reduce the amount of manual labor. Please meet with current supervisor(s) to refine the criteria further.
