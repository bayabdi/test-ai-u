'''
    Создайте простой веб-сервер (Flask, FastAPI).
    Напишите эндпойнт,
    который добавляет результат в гугл-таблицу и эндпойнт,
    который возвращает данные из гугл таблицы в виде JSON-объекта.
'''

import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import gspread

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREAD_SHEET_ID = "16HfS31RT_G-XCOz8m40y1EOG19eYF0Z0L-pBzXYV6Rg"


def get_crendentials():
    credentials = service_account.Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
    return credentials


def get_all():
    credentials = get_crendentials()
    service = build("sheets", "v4", credentials=credentials)
    sheets = service.spreadsheets()

    result = sheets.values().get(spreadsheetId=SPREAD_SHEET_ID, range="Sheet2!A:B").execute()
    values = result.get("values", [])
    
    for row in values:
        print(row)
    
    return values


def append_values_to_sheet(sheet_title, values_to_append):
    credentials = get_crendentials()
    service = build("sheets", "v4", credentials=credentials)
    sheets = service.spreadsheets()
    print(values_to_append)

    # Get the range of the sheet
    range_ = f"{sheet_title}!A1:B"  # Adjust the range as needed

    # Prepare the request body
    body = {
        'values': [values_to_append]
    }

    # Make the API request to append values
    result = sheets.values().append(
        spreadsheetId=SPREAD_SHEET_ID,
        range=range_,
        valueInputOption='RAW',
        body=body
    ).execute()

    print(f"Values appended to {sheet_title} successfully!")
