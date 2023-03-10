from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import urllib.request
import os
from dotenv import load_dotenv

load_dotenv()

PATH_WEBDRIVER = 'C:\DEVELOPMENT\msedgedriver.exe'
# check the location in "edge://version"
PATH_TO_BROWSER_PROFILE = r'C:\Users\FaMiLy\AppData\Local\Microsoft\Edge\User Data\Profile 2'

# Adding webdriver settings(arguments) before initializing it.
opt = webdriver.EdgeOptions()

# Some Basic Arguments
opt.add_argument("start-maximized")
opt.add_argument("disable-infobars")
opt.add_argument("--disable-extensions")
opt.add_argument(f"user-data-dir={PATH_TO_BROWSER_PROFILE}")
# This is a sample Python script.

# Starting the Driver and opening website page
bot = webdriver.Edge(executable_path=PATH_WEBDRIVER, options=opt)
bot.implicitly_wait(5)
bot.get(
    'https://sida.medu.ir/#/login')
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# ____________________ SIGN IN ______________________
bot.find_element(By.ID, value='userName').send_keys(os.environ.get('SIDA_USERNAME'))
sleep(3)
bot.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div/fieldset/div[3]/div[2]/div[2]/span/input').click()
bot.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div/fieldset/div[3]/div[2]/div[2]/span/input').send_keys(os.environ.get('SIDA_PASSWORD'))
sleep(5)
bot.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div/fieldset/div[3]/div[4]/button').click()
sleep(5)

# ______________________ CHANGE EDUCATION YEAR ____________________
bot.find_element(By.XPATH,
                     value=f"/html/body/div[1]/div/div[1]/nav/div/div/ul/li[3]/span").click()
sleep(3)
bot.find_element(By.XPATH,
                     value=f"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/table/tbody/tr[1]").click()
sleep(1)
bot.find_element(By.XPATH,
                     value=f"/html/body/div[1]/div/div/div[1]/div[3]/button").click()
sleep(2)
# ______________________ LOGS PART ____________________
bot.find_element(By.XPATH, value="/html/body/div[1]/div/div[3]/div[1]/ul/li[2]").click()  #عملیات ضمن سال
sleep(1)
bot.find_element(By.XPATH, value="/html/body/div[1]/div/div[3]/div[3]/div/div[5]/div[1]/a").click()  #کارنامه
sleep(1)
bot.find_element(By.XPATH, value="/html/body/div[1]/div/div[3]/div[3]/div/div[5]/div[2]/div/ul/li[4]").click()  #کارنامه گروهی
sleep(2)
bot.find_element(By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/ui-view/div/div/div[2]/span[1]/input").click()  #کارنامه نیم سال
sleep(2)

for i in range(1, 8):
    bot.find_element(By.XPATH,
                     value="/html/body/div[1]/div/div[2]/div/div/ui-view/div/div/div[1]/popup-class-room/div/div[2]/span").click()  # انتخاب کلاس
    sleep(3)
    bot.find_element(By.XPATH,
                     value=f"/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/table/tbody/tr[{i}]").click()    # انتخاب کلاس ها
    bot.find_element(By.XPATH,
                     value=f"/html/body/div[1]/div/div/div/div[3]/button").click()    # انتخاب اوکی
    sleep(3)
    bot.find_element(By.XPATH,
                     value=f"/html/body/div[1]/div/div[2]/div/div/ui-view/div/div/div[3]/div[1]/div/ul/li[2]/button").click()    # کارنامه گروهی
    sleep(5)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    main_div = bot.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div')
    res = main_div.find_elements(By.XPATH, 'div')
    print(res, '\n', len(res))

    for i in range(1, len(res) + 1):
        try:
            student_name = bot.find_element(By.XPATH,
                                            value=f"/html/body/div[1]/div/div/div/div[2]/div/div/div/div[{i}]/div[1]/div[3]/label[2]").text
            student_lastname = bot.find_element(By.XPATH,
                                                value=f"/html/body/div[1]/div/div/div/div[2]/div/div/div/div[{i}]/div[1]/div[3]/label[4]").text
            student_score = float(bot.find_element(By.XPATH,
                                                   value=f"/html/body/div[1]/div/div/div/div[2]/div/div/div/div[{i}]/table/tbody/tr[16]/td[5]/p").text)
            student_class = bot.find_element(By.XPATH,
                                             value=f"/html/body/div[1]/div/div/div/div[2]/div/div/div/div[{i}]/div[1]/div[2]/label[10]").text
            student_img = bot.find_element(By.XPATH,
                                           value=f"/html/body/div[1]/div/div/div/div[2]/div/div/div/div[{i}]/div[1]/div[4]/img").get_attribute("src")

            if 19 <= student_score < 19.5:
                student_round_score = 19
                print(student_name, student_lastname, student_score, '\n')
                urllib.request.urlretrieve(student_img,
                                           f"{student_class}/19-19.49/{student_name}-{student_lastname}-{student_score}.png")
            elif 19.5 <= student_score < 20:
                student_round_score = 19.5
                print(student_name, student_lastname, student_score, '\n')
                urllib.request.urlretrieve(student_img,
                                           f"{student_class}/19.5-19.99/{student_name}-{student_lastname}-{student_score}.png")
            elif student_score == 20:
                student_round_score = 20
                print(student_name, student_lastname, student_score, '\n')
                urllib.request.urlretrieve(student_img,
                                           f"{student_class}/20/{student_name}-{student_lastname}-{student_score}.png")
        except NoSuchElementException:
            pass

    bot.find_element(By.XPATH,
                     value=f"/html/body/div[1]/div/div/div/div[1]/i").click()   #بستن کارنامه ها


print("-"*20)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

