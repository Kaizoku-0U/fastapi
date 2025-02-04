# fastAPI API

follow these instructions to get the application running.

command to install dependecies :
"pip install -r requirements.txt"

we have 2 sctrips for data transformation and data loading.

use excel_json.py to read the excel and convert it to json , we have the output file if u want u can generate it again using the following command.
"python excel_json.py"

use insert_data.py to insert the output of the above script.
use the following command to insert the excel data to sql.
"python insert_data.py"

to up the backed of the application u can use :

"python main.py"

since we only have a single api in the requirements :

to test this we might have to manually enter the api route "http://localhost:8000/wells/{api_well_number}"
eg:"http://localhost:8000/wells/34059243520000"