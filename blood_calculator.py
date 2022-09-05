def interface():
    print("Blood Calculator")
    print("Options:")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter your choice: ")
        if choice == '9':
            return

def user_input():
    user_HDL = input("Type your HDL result")
    return int(user_HDL) #since the input is string by default


interface()
