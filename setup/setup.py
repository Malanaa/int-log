import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

sheet_id = "1hwHOCX9JFfZgiEYGATgCT8z1_-7ZGvKkP6nKAY7ICS0"


creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet = client.open_by_key("1hwHOCX9JFfZgiEYGATgCT8z1_-7ZGvKkP6nKAY7ICS0")
