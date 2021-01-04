from selenium import webdriver
import time, platform
from tkinter import *
from colorama import init, Fore, Back
#Copyright
print(f"{Fore.GREEN}©Jack Green 2020{Fore.RESET}")

def EXITING_text():
    print(f"{Back.RED+Fore.WHITE}EXITING{Back.RESET+Fore.RESET}")
# Specifies the path to the chrome driver and makes "driver" the browser variable
def NO_NEW_UPDATES_text():
    print(f"{Back.YELLOW+Fore.BLACK}NO NEW UPDATES WERE FOUND{Back.RESET+Fore.RESET}")
def DirectoryNo():
    print(f"{Back.RED+Fore.WHITE}PLEASE CHANGE THE DIRECTORY AND RUN THE PROGRAM AGAIN!")
    EXITING_text()
    exit()
#MACOS
if platform.system() == 'Darwin':
    PATH = "/Library/Application Support/chromedriver"
    print(f"OS: {Back.WHITE+Fore.BLACK}MacOS{Back.RESET+Fore.RESET}")
    path_confirm = input(f"{Fore.YELLOW}is this the correct directory of your chromedriver?: '{PATH}'\n[Y/N]{Fore.RESET}")
    if path_confirm == "N" or path_confirm == "n" or path_confirm == "no":
        DirectoryNo()
#WINDOWS
if platform.system() == 'Windows':
    PATH = "C:\chromedriver.exe"
    print(f"OS: {Back.BLUE+Fore.WHITE}WINDOWS{Back.RESET+Fore.RESET}")
    path_confirm = input(f"{Fore.YELLOW}is this the correct directory of your chromedriver?: '{PATH}'\n[Y/N]{Fore.RESET}")
    if path_confirm == "N" or path_confirm == "n" or path_confirm == "no":
        DirectoryNo()
driver = webdriver.Chrome(PATH)

# Defines BVB website URL
driver.get("https://www.bvb.ch/de/aktuelle-informationen/verkehrsinformationen/")
time.sleep(2)
# find all elememts of "a" (anchor tag) within the div with an id of "content"
elements = driver.find_elements_by_css_selector("div#content a")

# the first time the for loop runs tab is 1 so it switches to the first tab and then gets incremented
# the second time it is 2 so it always switches to the new tab when the for loop starts again
tab = 1
# page elements
h3_title_list = []
for element in elements:
    # get the hrefs of the "a" tags
    href = element.get_attribute("href")
    print(href)
    # new tab
    driver.execute_script("window.open('');")
    # switch to new tab
    driver.switch_to_window(driver.window_handles[tab])
    time.sleep(0.5)
    # open link in the new tab
    driver.get(href)
    time.sleep(1)
    # get h3_title
    h3_title = driver.find_element_by_css_selector("div.col-xs-12 h3").text
    h3_title_list.append(h3_title)
    print(h3_title_list)
    # switch back to main tab
    driver.switch_to_window(driver.window_handles[0])
    # increment
    tab+=1
    time.sleep(2)

# Check if there are elements if not gives error and exits
try:
    print(h3_title_list[0])
except IndexError:
    NO_NEW_UPDATES_text()
    EXITING_text()
    driver.quit()
    quit()
    
# EMAIL SEND
def SendEmail():
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib
    #from Tkinter import *
    sender_email_input = input(str(f"{Fore.GREEN}Enter the email you would like to send FROM: {Fore.RESET}"))
    sender_email = sender_email_input

    rec_email_input = input(str(f"{Fore.GREEN}Enter the email you would like to send TO: {Fore.RESET}"))
    rec_email = rec_email_input
    # Password input GUI to go here

    password = input(str("Please enter your password: "))
        
    msg = MIMEMultipart()

    msg['From'] = sender_email
    msg['To'] = rec_email
    msg['Subject'] = h3_title_list[0]
    

    html = f"<h1>{str(h3_title_list[0])}</h1><br><img src='http://jackgreen.ch/bvb_automation/bvb.png' style='background: black;'></img><br>view the sourcecode on github<a href='https://github.com/jasekk99/BVB-Verkehrsinformation-Automation'><img src='http://jackgreen.ch/bvb_automation/github.png' style='width: 30px;'></img></a>"
    msg.attach(MIMEText(html, 'html'))


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    print("Login success")
    server.sendmail(sender_email, rec_email, text)
    print("Email sent to", rec_email)
    server.quit()

SendEmail()
time.sleep(2)
driver.quit()