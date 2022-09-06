def interface():
    print("Blood Calculator")
    print("Options:")
    print("1 - Analyze HDL")
    print("2 - Analyze LDL")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()
        elif choice == '2':
            LDL_driver()

def user_input():
    user_value = input("Enter your value: ")
    return int(user_value) #since the input is string by default

#HDL
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

#LDL
def check_LDL(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value <= 159: #python can use this notation for compound inequality
        return "Borderline High"
    elif 160 <= LDL_value <= 189:
        return "High"
    else:
        return "Very High"  

def LDL_driver():
    LDL_value = user_input()
    answer = check_LDL(LDL_value)
    output_LDL_result(LDL_value, answer) #because function doesn't process this simultaneously, output_LDL_result can be defined later

def output_LDL_result(LDL_value, charac):
    print("The results for an LDL value of {} is {}".format(LDL_value, charac))

#Total cholesterol
def check_total(HDL_value, LDL_value):
    total = HDL_value + LDL_value
    if total<200:
        return "Normal"
    elif 200 <= total <= 239:
        return "Borderline High"
    else:
        return "High"

    


interface() #this line in main part of script will make the interface run
