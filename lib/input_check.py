#input check
def check(question_string, list):
    check = True
    while check:
        var = input(question_string)
        var = var.upper()
        if var in list:
            check = False 
        else:
            print(f"Invalid Input, List of acceptableInput => {list[0:]}")
    return var


