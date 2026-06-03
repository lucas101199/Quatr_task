# Quatr_task
This script fetch and convert the latest SEC 10-K report from companies to PDF.
aLL the PDF are saved under the PDF folder

### Install dependencies
First, you will need install the dependencies present in the requirement.txt file
Run:
```
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

### API endpoint
In order to get the endpoint running you will need to run the Uvicorn server.

```
uvicorn main:app
```
Once it's running connect to the address http://127.0.0.1:8000
then to retrieve a specific PDF just add the line below after the server address
```
/companies/{cik}/latest-10k
```
You will need to replace the `{cik}` with the CIK number of the company

If you want to retrieve all PDFs at once just add the line below
```
/companies/latest-10k-all
```
You can also access the API docs at this address:
```
http://127.0.0.1:8000/docs
```

### Main function
If you don't want to run a server you can always run the program with to get all PDFs
```
python main.py
```
