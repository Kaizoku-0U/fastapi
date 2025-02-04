import pandas as pd
import json

# Read the Excel file
excel_file = '20210309_2020_1 - 4 (1) (1) (1) (1).xls'
df = pd.read_excel(excel_file, engine='xlrd')

json_array = df.to_dict(orient='records') #(I could have used the orm query here itself to insert the data to the db but I am writing a seperate script for this since it was in requirements and easy for debugging)

with open('output.json', 'w') as json_file:
    json.dump(json_array, json_file, indent=4)
