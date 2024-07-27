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
        print("Succesfully logged application")

             
def get_info():
    #Gathering Input from user 
    company_name = input("Company Name: ")
    acc_rejec = check("Accepted/Rejected (A/R/ N/A): ", ["A","R","N/A"])
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

    return id_new

def add_internship(ws, row_num, id_intern,company_name,acc_rejec,link,note):
    ws.update_acell(f"A{row_num}", id_intern)
    ws.update_acell(f"B{row_num}", company_name)
    ws.update_acell(f"C{row_num}", datetime.today().strftime('%Y-%m-%d'))
    ws.update_acell(f"D{row_num}", acc_rejec)
    ws.update_acell(f"E{row_num}", link)
    ws.update_acell(f"F{row_num}", note)
    print("Succesfully logged application")

def find_internship(name):
    found_cell = ws.find(name)
    if found_cell != None:
        values = ws.row_values(found_cell.row)
        print(f"ID: {values[0]}")
        print(f"Company: {values[1]}")
        print(f"Date: {values[2]}")
        print(f"Status: {values[3]}")
        print(f"Links: {values[4]}")
        print(f"Notes: {values[5]}")
    else:
        print("application not found")

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


company_name, acc_rejec, link, note = get_info()
id_intern = id_assign(ws)
row_num = id_intern + 2
add_internship(ws, row_num, id_intern, company_name, acc_rejec, link, note)


