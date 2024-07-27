import gspread
from google.oauth2.service_account import Credentials
import os
from dotenv import load_dotenv

load_dotenv()
path_name  = os.getenv("creds_var")
scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]


creds = Credentials.from_service_account_file(path_name, scopes=scopes)
client = gspread.authorize(creds)
