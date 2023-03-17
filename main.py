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


class Automation:
    def __init__(self):
        # Adding webdriver settings(arguments) before initializing it.
        self.opt = webdriver.EdgeOptions()

        # Some Basic Arguments
        self.opt.add_argument("start-maximized")
        self.opt.add_argument("disable-infobars")
        self.opt.add_argument("--disable-extensions")
        self.opt.add_argument(f"user-data-dir={PATH_TO_BROWSER_PROFILE}")

        # Starting the Driver
        self.bot = webdriver.Edge(executable_path=PATH_WEBDRIVER, options=self.opt)

    def open_website(self):
        self.bot.get('https://sida.medu.ir/#/login')

    def sign_in(self):
        self.bot.find_element(By.ID, value='userName').send_keys(os.environ.get('SIDA_USERNAME'))
        sleep(3)
        self.bot.find_element(By.XPATH,
                              value='/html/body/div[1]/div[2]/div/fieldset/div[3]/div[2]/div[2]/span/input').click()
        self.bot.find_element(By.XPATH,
                              value='/html/body/div[1]/div[2]/div/fieldset/div[3]/div[2]/div[2]/span/input').send_keys(
            os.environ.get('SIDA_PASSWORD'))
        bot.execute_script("alert('کد امنیتی را خودتان وارد کنید. دقت داشته باشید که دکمه ی ورود را به هیچ عناون کلیک نکنید. خود برنامه این کار را میکند.')")
        sleep(5)
        self.bot.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div/fieldset/div[3]/div[4]/button').click()
        sleep(5)

    def change_education_year(self):
        self.bot.find_element(By.XPATH,
                              value=f"/html/body/div[1]/div/div[1]/nav/div/div/ul/li[3]/span").click()
        sleep(3)
        self.bot.find_element(By.XPATH,
                              value=f"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/table/tbody/tr[1]").click()
        sleep(1)
        self.bot.find_element(By.XPATH,
                              value=f"/html/body/div[1]/div/div/div[1]/div[3]/button").click()
        sleep(2)

    def getting_students_logs(self):
        self.bot.find_element(By.XPATH, value="/html/body/div[1]/div/div[3]/div[1]/ul/li[2]").click()  # عملیات ضمن سال
        sleep(1)
        self.bot.find_element(By.XPATH,
                              value="/html/body/div[1]/div/div[3]/div[3]/div/div[5]/div[1]/a").click()  # کارنامه
        sleep(1)
        self.bot.find_element(By.XPATH,
                              value="/html/body/div[1]/div/div[3]/div[3]/div/div[5]/div[2]/div/ul/li[4]").click()  # کارنامه گروهی
        sleep(2)
        self.bot.find_element(By.XPATH,
                              value="/html/body/div[1]/div/div[2]/div/div/ui-view/div/div/div[2]/span[1]/input").click()  # کارنامه نیم سال
        sleep(2)

        for i in range(1, 8):
            self.bot.find_element(By.XPATH,
                                  value="/html/body/div[1]/div/div[2]/div/div/ui-view/div/div/div[1]/popup-class-room/div/div[2]/span").click()  # انتخاب کلاس
            sleep(3)
            self.bot.find_element(By.XPATH,
                                  value=f"/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/table/tbody/tr[{i}]").click()  # انتخاب کلاس ها
            self.bot.find_element(By.XPATH,
                                  value=f"/html/body/div[1]/div/div/div/div[3]/button").click()  # انتخاب اوکی
            sleep(3)
            self.bot.find_element(By.XPATH,
                                  value=f"/html/body/div[1]/div/div[2]/div/div/ui-view/div/div/div[3]/div[1]/div/ul/li[2]/button").click()  # کارنامه گروهی
            sleep(5)

            main_div = self.bot.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div')
            res = main_div.find_elements(By.XPATH, 'div')
            print(res, '\n', len(res))

            for i in range(1, len(res) + 1):
                try:
                    student_name = self.bot.find_element(By.XPATH,
                                                         value=f"/html/body/div[1]/div/div/div/div[2]/div/div/div/div[{i}]/div[1]/div[3]/label[2]").text
                    student_lastname = self.bot.find_element(By.XPATH,
                                                             value=f"/html/body/div[1]/div/div/div/div[2]/div/div/div/div[{i}]/div[1]/div[3]/label[4]").text
                    student_score = float(self.bot.find_element(By.XPATH,
                                                                value=f"/html/body/div[1]/div/div/div/div[2]/div/div/div/div[{i}]/table/tbody/tr[16]/td[5]/p").text)
                    student_class = self.bot.find_element(By.XPATH,
                                                          value=f"/html/body/div[1]/div/div/div/div[2]/div/div/div/div[{i}]/div[1]/div[2]/label[10]").text
                    student_img = self.bot.find_element(By.XPATH,
                                                        value=f"/html/body/div[1]/div/div/div/div[2]/div/div/div/div[{i}]/div[1]/div[4]/img").get_attribute(
                        "src")

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

            self.bot.find_element(By.XPATH,
                                  value=f"/html/body/div[1]/div/div/div/div[1]/i").click()  # بستن کارنامه ها


bot = Automation()
bot.open_website()
