import gspread
from setup.setup import client 

email = 'abdullahdotpy@gmail.com'

try:
    sh = client.open('internshipLog_test')
except gspread.exceptions.SpreadsheetNotFound:
    sh = client.create('internshipLog_test')
    sh.share(email, perm_type='user', role='writer')

