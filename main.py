from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
import urllib.request
import os
from dotenv import load_dotenv
from selenium.webdriver.edge.service import Service

load_dotenv()
PATH_WEBDRIVER = 'C:\DEVELOPMENT\msedgedriver.exe'
# check the location in "edge://version"
PATH_TO_BROWSER_PROFILE = r'C:\Users\FaMiLy\AppData\Local\Microsoft\Edge\User Data\Profile 2'
WEBSITE_URL = 'https://sida.medu.ir/#/login'

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
        service = Service(PATH_WEBDRIVER)
        self.bot = webdriver.Edge(service=service, options=self.opt)
        self.alert = Alert(self.bot)

    def open_website(self):
        self.bot.implicitly_wait(5)
        self.bot.get(WEBSITE_URL)

    def sign_in(self):
        self.bot.implicitly_wait(5)
        self.bot.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/fieldset/div[3]/div[1]/div/span/input").send_keys(os.environ.get('SIDA_USERNAME'))
        self.bot.implicitly_wait(5)
        self.bot.find_element(By.XPATH,
                              value='/html/body/div[1]/div[2]/div/fieldset/div[3]/div[2]/div/span/input').send_keys(
            os.environ.get('SIDA_PASSWORD'))
        sleep(3)
        self.bot.find_element(By.XPATH,
                              value='/html/body/div[1]/div[2]/div/fieldset/div[3]/div[3]/div[1]/div/span/input').click()
        self.bot.execute_script("alert('کد امنیتی را خودتان وارد کنید. دقت داشته باشید که دکمه ی ورود را به هیچ عناون کلیک نکنید. خود برنامه این کار را میکند.')")
        sleep(7)
        try:
            self.alert.accept()
        except NoAlertPresentException:
            pass
        finally:
            WebDriverWait(self.bot, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                        "/html/body/div[1]/div[2]/div/fieldset/div[3]/div[4]/button"))).click()

    def change_education_year(self):
        self.bot.implicitly_wait(5)
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
                              value="/html/body/div[1]/div/div[3]/div[3]/div/div[5]/div[2]/div/ul/li[5]/a").click()  # کارنامه گروهی
        self.bot.implicitly_wait(5)
        self.bot.find_element(By.XPATH,
                              value="/html/body/div[1]/div/div[2]/div/div/ui-view/div/div/div[2]/span[1]/input").click()  # کارنامه نیم سال
        sleep(2)

        self.bot.find_element(By.XPATH,
                              value="/html/body/div[1]/div/div[2]/div/div/ui-view/div/div/div[1]/popup-class-room/div/div[2]/span").click()  # انتخاب کلاس
        number_of_classes = len(self.bot.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/table/tbody").find_elements(By.XPATH, "tr"))
        self.bot.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/i").click()       #بستن کلاسها
        for i in range(1, number_of_classes+1):
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

                    if not os.path.exists(f"{student_class}"):
                        os.mkdir(f"{student_class}")
                        os.mkdir(f"{student_class}/19-19.49")
                        os.mkdir(f"{student_class}/19.5-19.99")
                        os.mkdir(f"{student_class}/20")

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
bot.sign_in()
bot.change_education_year()
bot.getting_students_logs()

