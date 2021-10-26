from datetime import datetime
import os

clean = "cls"

username = ""
user_Input = ""

commands = """commands - 
help - get help
time - current time
quit - quit program
name - change username
date - current date
cls - clear terminal
homework - run the homework program
color - change text color (red, green, white, brown, black, cyan, blue, gray)"""

os.system(clean)
username = input("Enter Your username here: ")

txt = open("log.txt", 'w')
print("User named {0}".format(username), file=txt)


def change_color():
    color_check = input("what color do you want? ")
    red = '4'
    brown = '6'
    white = '7'
    green = 'a'
    black = '0'
    cyan = '3'
    blue = '1'
    gray = '8'
    if color_check == 'red' or user_Input == '4':
        os.system("color {0}".format(red))
    elif color_check == 'white' or user_Input == '7':
        os.system("color {0}".format(white))
    elif color_check == 'brown' or user_Input == '6':
        os.system("color {0}".format(brown))
    elif color_check == 'green' or user_Input == 'a':
        os.system("color {0}".format(green))
    elif color_check == 'black' or user_Input == '0':
        os.system("color {0}".format(black))
    elif color_check == 'cyan' or user_Input == '3':
        os.system("color {0}".format(cyan))
    elif color_check == 'blue' or user_Input == '1':
        os.system("color {0}".format(blue))
    elif color_check == 'gray' or user_Input == '8':
        os.system("color {0}".format(gray))
    else:
        print("Can't recognise color")
        print("User typed wrong color", file=txt)


while True:
    user_Input = input("{0}: ".format(username)).lower()
    if user_Input == "quit":
        print("User closed the program", file=txt)
        os.system('color 7')
        break
    elif user_Input == "time":
        Time_now = datetime.now()
        current_time = Time_now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        print("User checked the time", file=txt)
    elif user_Input == "help":
        print("User got help", file=txt)
        print(commands)
    elif user_Input == "name":
        username = input("Enter Your username here: ")
        print("user change his username to {0}".format(username), file=txt)
    elif user_Input == "date":
        Date_now = datetime.today().strftime('%Y-%m-%d')
        print("Current date =", Date_now)
        print("User checked the date", file=txt)
    elif user_Input == username:
        print("Why did you check for your name you stupid boi")
        print("User is dumb", file=txt)
    elif user_Input == 'cls':
        os.system('cls')
        print("User cleaned the terminal", file=txt)
    elif user_Input == "homework":
        print("The user initialized homework program", file=txt)
        print("HomeWork opening")
        os.system("py HomeWork.py")
    elif user_Input == "color":
        change_color()
    elif user_Input == user_Input:
        os.system(user_Input)
        print("The user used a cmd command", file=txt)
    else:
        print("{0}: {1}".format(username, user_Input), file=txt)

txt.close()
