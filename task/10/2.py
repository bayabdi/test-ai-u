'''
    Создайте простой веб-сервер (Flask, FastAPI).
    Напишите эндпойнт,
    который добавляет результат в гугл-таблицу и эндпойнт,
    который возвращает данные из гугл таблицы в виде JSON-объекта.
'''


from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import JSONResponse
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
import gspread
from oauth2client.service_account import ServiceAccountCredentials


app = FastAPI()
credentials = ServiceAccountCredentials.from_json_keyfile_name('your-credentials.json', ['https://spreadsheets.google.com/feeds'])
gc = gspread.authorize(credentials)

spreadsheet_key = 'your-spreadsheet-id'
worksheet_name = 'Sheet1'

@app.post("/add-to-google-sheet/")
async def add_to_google_sheet(value: str = Form(...)):
    try:
        worksheet = gc.open_by_key(spreadsheet_key).worksheet(worksheet_name)
        
        worksheet.append_row([value])
        
        return JSONResponse(content={"message": "Value added to Google Sheet successfully"}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/get-google-sheet-data/")
async def get_google_sheet_data():
    try:
        worksheet = gc.open_by_key(spreadsheet_key).worksheet(worksheet_name)
        values = worksheet.get_all_values()
        
        headers = values[0]
        data = [dict(zip(headers, row)) for row in values[1:]]
        
        return JSONResponse(content={"data": data}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
