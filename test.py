# Explicit Waits: wait for a special element to get loaded.
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get("http://somedomain/url_that_delays_loading")
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))

# Implicit Waits: just wait for a certain time.
driver.implicitly_wait(10)
driver.get("http://somedomain/url_that_delays_loading")

# Third and Easiest method
time.sleep(10)

find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")  # Full XPATH is usually the best.
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")

# "find_elements" is also a method to give you multiple elements in a list (object type).
# it is better to be used chaining with "find_element"
main_div = bot.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]')
divs = main_div.find_elements(By.XPATH, 'div')


form = bot.find_element(By.ID, value='userName')

form.click()
form.send_keys("12345")
form.send_keys(Keys.RETURN)  # You can use any keyboard keys, see Special Keys in the docs

""" Use your own browser profiles """
# Check the location in "edge://version"
PATH_TO_BROWSER_PROFILE = r'C:\Users\FaMiLy\...\Profile 2'
opt.add_argument(f"user-data-dir={PATH_TO_BROWSER_PROFILE}")


""" Your Selenium bot can stay more undetected as a bot with these args. """

options.add_argument('--no-sandbox')
# This argument tells Chrome to run without its sandbox security feature,
# which can be useful when running automated tests on a machine with limited resources or in a virtualized environment.

options.add_argument('--single-process')
# This argument tells Chrome to run in single-process mode,
# which can help with memory usage but may also impact performance.

options.add_argument('--disable-dev-shm-usage')
# This argument disables the use of /dev/shm for temporary file storage,
# which can improve performance when working with large datasets.

options.add_argument('--disable-blink-features=AutomationControlled'):
# This argument disables the AutomationControlled feature in the Chrome browser,
# which can help prevent certain types of automated scripts from running.

options.add_experimental_option('useAutomationExtension', False):
# This experimental option disables the Chrome automation extension,
# which is used by some automated testing frameworks.

options.add_experimental_option("excludeSwitches", ["enable-automation"]):
# This experimental option excludes the enable-automation switch,
# which is often used by websites to detect automated browser activity.

options.add_argument('Inspect > More Tools > Network Conditions'):
# This argument sets the user agent string for the Chrome browser,
# which can be useful for testing how websites behave under different browser conditions

options.add_argument('--proxy-server=%s' % ip)
# This command-line argument sets the proxy server for the Chrome browser.


# Making or Modifying a Var.:    (you can also use .env to make environ vars using dotenv package)
os.environ['JAVA_HOME'] = '/home / ihritik / jdk-10.0.1'


# Method to change the current working directory to the specified path.
os.chdir('E:/Tutorials/Code/6.Advanced/72 Day 72path')

# Check the working directory
os. getcwd()

# Make a new dir
os.mkdir(path="new folder")

