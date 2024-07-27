import gspread
from lib.input_check import check
from setup.setup import client 
from datetime import datetime


email = 'abdullahdotpy@gmail.com'

def setup_header(ws):
    ws.update_cell( 1, 1, "ID")
    ws.update_cell( 1, 2, "CompanyName")
    ws.update_cell( 1, 3, "DateApplied")
    ws.update_cell( 1, 4, "Accepted/Rejected")
    ws.update_cell( 1, 5, "Links")
    ws.update_cell( 1, 6, "Note")

def get_info():
    #Gathering Input from user 
    company_name = input("Company Name: ")
    acc_rejec = check("Accepted/Rejected (A/R): ", ["A","R","a","r"])
    link = input("Link: ")
    note = input("Additional Notes: ")

    return company_name, acc_rejec, link, note

def id_assign(ws):
    ids = ws.col_values(1)
    ids.remove(ids[0])

    id_new = 0 
    if len(ids) > 0:
        sorted(ids)
        id_new = int(ids[len(ids) - 1])
        id_new += 1
    else:
        id_new = 0 

    return id_new

try:
    sh = client.open('internshipLog_test')
    print("Spreadsheet found")
    ws = sh.sheet1
    setup_header(ws)
except gspread.exceptions.SpreadsheetNotFound:
    sh = client.create('internshipLog_test')
    sh.share(email, perm_type='user', role='writer')
    print("Spreadsheet created and shared")
    ws = sh.sheet1
    setup_header(ws)

id_intern = id_assign(ws)
company_name, acc_rejec, link, note = get_info()

