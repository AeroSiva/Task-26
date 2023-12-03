from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Data import data
from Locators import locators


class IMDB:
    def __init__(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver,10)
        self.actions = ActionChains(self.driver)

    def access_URL(self):
        try:
            self.driver.maximize_window()
            self.driver.get(data.IMDB_Data().URl)
        except Exception as selenium_error:
            print("Selenium Error: ", selenium_error)

    def fill_datas(self):
        try:
            # Clicking Expand all button
            expand_svg = self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.IMDB_Locators().expand_all_svg_xpath)))
            if not expand_svg.is_displayed():
                self.driver.execute_script("arguments[0].scrollIntoView(true);", expand_svg)
            expand_svg.click()
            print("Clicked Expand all")

            # Enter name to be searched
            name_box = self.wait.until(EC.element_to_be_clickable((By.ID,locators.IMDB_Locators().name_box_id)))
            if not name_box.is_displayed():
                self.driver.execute_script("arguments[0].scrollIntoView(true);", name_box)
            name_box.send_keys(data.IMDB_Data().name)
            print("name entered successfull")

            # Entering Birthday from data
            birthday_from_id = self.wait.until(EC.element_to_be_clickable((By.ID,locators.IMDB_Locators().birthday_from_id)))
            if not birthday_from_id.is_displayed():
                print("Entere birthday from conditiona")
                self.driver.execute_script("arguments[0].scrollIntoView(true);", birthday_from_id)
            self.driver.execute_script(f"arguments[0].value = '{data.IMDB_Data().birthday_from}';", birthday_from_id)
            print("birthday from filled successfull")

            # Entering Birthday to data
            birthday_to_id = self.wait.until(EC.element_to_be_clickable((By.ID,locators.IMDB_Locators().birthday_to_id)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", birthday_to_id)
            self.driver.execute_script(f"arguments[0].value = '{data.IMDB_Data().birthday_to}';", birthday_to_id)
            print("birthday to entered successfull")

            # Entering page topic entered to be quotes
            page_topic_quote = self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.IMDB_Locators().pg_quotes_xp)))
            print("page topic defined")
            if page_topic_quote.is_displayed():
                print("Entered into page topic conditional")
                parent_element = page_topic_quote.find_element(By.XPATH, "..")  # Move up to the parent element
                print("parent element defined")
                self.driver.execute_script("arguments[0].scrollIntoView(true);", parent_element)
            #self.driver.execute_script("arguments[0].scrollIntoView(true);", page_topic_quote)
            #ActionChains(self.driver).move_to_element(page_topic_quotes).click().perform()
            self.driver.execute_script("arguments[0].click();", page_topic_quote)
            print("page topic selected quotes")
            
            # Selecting gender to be male
            gender_identity = self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.IMDB_Locators().gen_iden_male_test_xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", gender_identity)
            self.driver.execute_script("arguments[0].click();", gender_identity)
            print("entered gender successfull")

            # Clicking adults to be included in chekbox
            check = self.wait.until(EC.element_to_be_clickable((By.ID, locators.IMDB_Locators().include_adults_id)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", check)
            self.driver.execute_script("arguments[0].click();", check)

            # Click the Search button
            search = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.IMDB_Locators.search_xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", search)
            self.driver.execute_script("arguments[0].click();", search)
            print("searched")
            return self.driver.title

        except Exception as e:
            print("Selenium Error: ",e)

if __name__ == "__main__":
    imdb = IMDB()
    imdb.access_URL()
    imdb.fill_datas()
    imdb.driver.quit()