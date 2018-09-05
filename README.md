# Glossary

This repository serves as the single source of truth for the Open Contracting Data Standard glossaries, which support the consistent use and translation of key terms. The glossaries are updated [in Google Sheets](https://docs.google.com/spreadsheets/d/1WGH9_mHYuF4JbK2tdyeckqsmj8v4HrRqDOEbKQ7CI4A/edit#gid=0), revision-controlled in this repository, and uploaded to Transifex, to be accessed by translators. For more information, see the [OCDS Development Handbook](https://ocds-standard-development-handbook.readthedocs.io/en/latest/standard/translation/terminology/).

## Usage

The `update.py` script uses the Google Sheets API to update the `glossaries` directory.

### 1. Install dependencies

Create and activate a virtual environment, then:

```
pip install google-api-python-client
```

### 2. Set-up authentication

* [Enable the Google Sheets API](https://developers.google.com/sheets/api/quickstart/python) for an account that has read access to the [glossary spreadsheet](https://docs.google.com/spreadsheets/d/1WGH9_mHYuF4JbK2tdyeckqsmj8v4HrRqDOEbKQ7CI4A/edit#gid=0)
* Save the `credentials.json` file in this directory (it is ignored by git)

### 3. Update glossaries

```
python update.py
```

The first time you run the script, you may need to complete in-browser authentication. 

### 4. Manually update Transifex glossaries

[Create](https://docs.transifex.com/setup/glossary/uploading-an-existing-glossary#uploading-your-csv-file) or [update](https://docs.transifex.com/setup/glossary/uploading-an-existing-glossary#updating-an-existing-glossary) the [glossaries](/glossaries) on [Transifex](https://www.transifex.com/OpenDataServices/). Alternately, instead of uploading one CSV at a time, the spreadsheet's [combined tab](https://docs.google.com/spreadsheets/d/1WGH9_mHYuF4JbK2tdyeckqsmj8v4HrRqDOEbKQ7CI4A/edit#gid=1568901331), downloaded as CSV, can be used for this.
