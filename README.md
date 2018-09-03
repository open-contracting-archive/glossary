# Glossary

This repository stories copies of the Open Contracting Data Standard glossary. 

The glossary supports consistent use and translation of terms. 

More details of the terminology and glossary process can be found in the [standard development handbook](https://ocds-standard-development-handbook.readthedocs.io/en/latest/standard/translation/terminology/#definition). 

## Updating glossaries

This repository stores a revision controlled copy of the glossaries.

Glossaries are currently edited [using Google sheets](https://docs.google.com/spreadsheets/d/1WGH9_mHYuF4JbK2tdyeckqsmj8v4HrRqDOEbKQ7CI4A/edit#gid=0), with a copy of the glossary mirrored here, and in the Transifex translation platforms. 

## Synchronisation

The update.py script uses the Google Spreadsheet API to update the glossaries folder. 

**Step 1: Install dependencies**

```
virtualenv -p python3 .ve
source .ve/bin/activate
pip install -r requirements.txt
```

**Step 2: Set-up authentication.**

Follow the instructions at https://developers.google.com/sheets/api/quickstart/python to enable the Google Spreadsheet API for an account that has read access to the glossary spreadsheet. 

Save the credentials.json file in this folder.

**Step 3: Run and authenticate**

```
python update.py
```

The first time you run the script you may need to complete in-browser authentication. 

**Step 4: Manually update transifex glossaries**

The combined tab of the spreadsheet, downloaded as CSV, can be used for this. 

[Create](https://docs.transifex.com/setup/glossary/uploading-an-existing-glossary#uploading-your-csv-file) or [update](https://docs.transifex.com/setup/glossary/uploading-an-existing-glossary#updating-an-existing-glossary) the [glossaries](/glossaries) on [Transifex](https://www.transifex.com/OpenDataServices/).
