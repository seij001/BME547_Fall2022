def interface():
    print("Blood Calculator")
    print("Options:")
    print("1 - Analyze HDL")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()

def user_input():
    user_HDL = input("Enter your HDL result: ")
    return int(user_HDL) #since the input is string by default

def check_HDL(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value <60: #python can use this notation for compound inequality
        return "Borderline Low"
    else:
        return "Low"

def HDL_driver():
    HDL_value = user_input()
    answer = check_HDL(HDL_value)
    output_HDL_result(HDL_value, answer)

def output_HDL_result(HDL_value, charac):
    print("The results for an HDL value of {} is {}".format(HDL_value, charac))
    

interface() #this line in main part of script will make the interface run

