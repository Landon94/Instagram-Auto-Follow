from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Constants import USERNAME, PASSWORD, USER_FOLLOW
import time


class InstagramBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options = chrome_options)

    def login(self, username, usr_password):
        self.driver.get("https://www.instagram.com/accounts/login/?hl=en")
        time.sleep(5)

        email = self.driver.find_element(By.XPATH, value = '//*[@id="loginForm"]/div/div[1]/div/label/input')

        time.sleep(3)
        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')

        email.send_keys(username)
        password.send_keys(usr_password)

        login = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button/div')
        login.click()

        time.sleep(6)

        off_save_login_info = self.driver.find_element(By.XPATH, value="//div[contains(text(), 'Not now')]")
        off_save_login_info.click()

        time.sleep(4)

    def follow(self, user_to_follow):
        #Click on Search Icon
        search_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[name()='svg' and @aria-label='Search']"))
        )
        search_icon.click()

        time.sleep(3)

        #Types into search bar
        self.driver.switch_to.active_element.send_keys(user_to_follow)

        time.sleep(3)

        a_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
        )

        filtered_search = [link for link in a_elements if user_to_follow.lower() in link.text.strip().lower()]

        #Clicks on top result from search
        filtered_search[1].click()

        time.sleep(3)

        #Clicks follow button
        button_follow = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'x1nhvcw1')]//button"))
        )
        button_follow.click()


def main():
    bot = InstagramBot()

    try:
        bot.login(USERNAME, PASSWORD)
        bot.follow(USER_FOLLOW)
        print("Successfully Followed")
    except Exception as e:
        print(f"Unexpected error as {e}")
    finally:
        bot.driver.quit()


if __name__ == "__main__":
    main()