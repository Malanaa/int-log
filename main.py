import gspread
import os
import dotenv
from lib.input_check import check
from lib.compare_string_natural import similar_string
from setup.setup import client 
from datetime import datetime


dotenv.load_dotenv()
email  = os.getenv("email")

'''

This is how I keep track of my internship applications

'''

def setup_header(ws):
        ws.update_cell( 1, 1, "ID")
        ws.update_cell( 1, 2, "CompanyName")
        ws.update_cell( 1, 3, "DateApplied")
        ws.update_cell( 1, 4, "Accepted/Rejected")
        ws.update_cell( 1, 5, "Links")
        ws.update_cell( 1, 6, "Additional Notes")
            
def get_info():
    #Gathering Input from user 
    company_name = input("Company Name: ")
    acc_rejec = check("Accepted/Rejected/Pending (A/R/P): ", ["A","R","P"])
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
    print("\nSuccesfully logged application.")

def find_internship(name):
    found_cell = ws.find(name)
    if found_cell != None:
        values = ws.row_values(found_cell.row)
        print(f"\nID: {values[0]}")
        print(f"Company: {values[1]}")
        print(f"Date: {values[2]}")
        print(f"Status: {values[3]}")
        print(f"Links: {values[4]}")
        print(f"Additional Notes: {values[5]}")
    else:
        print("\nExact string not found. Trying another search method.")
        company_names = ws.col_values(2)
        company_names.remove(company_names[0])
        for i in range(len(company_names)):
            similarBool = similar_string(name, company_names[i])
            if similarBool:
                new_name = company_names[i]
                found_cell = ws.find(new_name)
                values = ws.row_values(found_cell.row)
                print(f"\nID: {values[0]}")
                print(f"Company: {values[1]}")
                print(f"Date: {values[2]}")
                print(f"Status: {values[3]}")
                print(f"Links: {values[4]}")
                print(f"Additional Notes: {values[5]}")
                return True 
        print("Application really not found.")
                
def find_internship_row(name):
    found_cell = ws.find(name)
    if found_cell != None:
        return found_cell.row
    else:
        print("\nExact string not found. Trying another search method")
        company_names = ws.col_values(2)
        company_names.remove(company_names[0])
        for i in range(len(company_names)):
            similarBool = similar_string(name, company_names[i])
            if similarBool:
                new_name = company_names[i]
                found_cell = ws.find(new_name)
                return found_cell.row
        print("Application really not found.")

def current_status(name):
    found_cell = ws.find(name)
    if found_cell != None:
        values = ws.row_values(found_cell.row)
        print(f"Current status: {values[3]}")
    else:
        print("\nExact string not found. Trying another search method")
        company_names = ws.col_values(2)
        company_names.remove(company_names[0])
        for i in range(len(company_names)):
            similarBool = similar_string(name, company_names[i])
            if similarBool:
                new_name = company_names[i]
                found_cell = ws.find(new_name)
                values = ws.row_values(found_cell.row)
                print(f"Current status: {values[3]}")
                return True
        print("Application really not found.")

def update_status(name, new_status):
    row_num = find_internship_row(name)
    ws.update_acell(f"D{row_num}", new_status)
    print("\nStatus succesfully updated")

try:
    sh = client.open('internshipLog')
    print("\nSpreadsheet found")
    ws = sh.sheet1
    setup_header(ws)
except gspread.exceptions.SpreadsheetNotFound:
    sh = client.create('internshipLog')
    sh.share(email, perm_type='user', role='writer')
    print("\nSpreadsheet created and shared")
    ws = sh.sheet1
    setup_header(ws)

def main():

    companies = ws.col_values(2)
    print(f"\nTotal Applications: {len(companies) - 1}")

    loop = True
    while loop:

        choice = check(''' 
log_application(L) | find_application(F) | update_application_status(U) | Exit(E)        
enter_choice: ''', ["L","F","U","E"])

        if choice == 'L':
            company_name, acc_rejec, link, note = get_info()
            id_intern = id_assign(ws)
            row_num = id_intern + 2
            add_internship(ws, row_num, id_intern, company_name, acc_rejec, link, note)
        elif choice == 'F':
            name = input('\nName of Company: ')
            found_internship = find_internship(name)
        elif choice == 'U':
            name = input('\nName of Company: ')
            status = current_status(name)
            new_status = check("\nAccepted/Rejected/Pending (A/R/P): ", ["A","R","P"])
            update_status(name, new_status)
        elif choice == "E":
            loop = False
    

    print("\nIt's joever")

main()