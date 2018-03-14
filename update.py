# See https://developers.google.com/sheets/api/quickstart/python
import argparse
import csv
import httplib2
import os
import re

from apiclient import discovery
from oauth2client import client, tools
from oauth2client.file import Storage

flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)

    credential_path = os.path.join(credential_dir, 'sheets.googleapis.com-python-quickstart.json')
    store = Storage(credential_path)
    credentials = store.get()

    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store, flags)

    return credentials


# See http://openpyxl.readthedocs.io/en/default/_modules/openpyxl/utils/cell.html#get_column_letter
def get_column_letter(col_idx):
    letters = []
    while col_idx > 0:
        col_idx, remainder = divmod(col_idx, 26)
        # check for exact division and borrow if needed
        if remainder == 0:
            remainder = 26
            col_idx -= 1
        letters.append(chr(remainder + 64))
    return ''.join(reversed(letters))


def formatted(name):
    # See https://docs.transifex.com/setup/glossary/uploading-an-existing-glossary
    name = name.lower().strip()

    # See https://www.transifex.com/explore/languages/
    name = name.replace('-', '_')

    # Restore the letter case of the locale.
    name = re.sub(r'\A((?:comment_)?[a-z]{2}_)([a-z]{2})\Z', lambda m: m.group(1) + m.group(2).upper(), name)

    return name


def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryServiceUrl = 'https://sheets.googleapis.com/$discovery/rest?version=v4'
    service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryServiceUrl)

    spreadsheetId = '1WGH9_mHYuF4JbK2tdyeckqsmj8v4HrRqDOEbKQ7CI4A'
    spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheetId).execute()

    valid_headers = ('term', 'pos', 'comment')

    for sheet in spreadsheet['sheets']:
        properties = sheet['properties']
        gridProperties = properties['gridProperties']
        title = properties['title']

        _range = "'{}'!A1:{}{}".format(
            properties['title'],
            get_column_letter(gridProperties['columnCount']),
            gridProperties['rowCount'])

        result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=_range).execute()

        if title == 'Source':
            basename = 'en'
        else:
            basename = formatted(title)

        comment_header = 'comment_{}'.format(basename)

        with open(os.path.join('glossaries', '{}.csv'.format(basename)), 'w') as f:
            writer = csv.writer(f, lineterminator='\n')

            indices = []
            headers = []

            for index, header in enumerate(result['values'][0]):
                # 'id' will otherwise match the language code regular expression.
                if index == 0:
                    continue

                header = formatted(header)

                # 'Definition' is used in Google Sheets for greater clarity for translators.
                if header.startswith('definition'):
                    header = header.replace('definition', 'comment')

                if header in valid_headers or header in (basename, comment_header):
                    indices.append(index)
                    headers.append(header)

            writer.writerow(headers)
            for row in result['values'][1:]:
                if len(row) > 1 and row[1]:
                    writer.writerow([row[index] if index < len(row) else None for index in indices])


if __name__ == '__main__':
    main()
