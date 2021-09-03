from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import unittest
import yaml
import warnings


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument('--disable-blink-features=AutomationControlled')

        self.driver = webdriver.Chrome(options=option)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://haveibeenpwned.com/")
        self.search_bar = self.driver.find_element(By.ID, "Account")

        self.emails = [
            "test@something.com",
            "qwerty@somehting.com",
            "katryna.tkachenko@gmail.com",
            "test@gmail.com",
            "kate.tkachenko@mail.ru",
            "test@test.com"
        ]

    def tearDown(self):
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        self.driver.close()

    def test_first_scenario(self):
        # First scenario:
        email = "test@something.com"
        self.search_bar.send_keys(email)
        self.driver.find_element(By.ID, "searchPwnage").click()

        self.wait.until(
            ec.visibility_of_element_located((By.XPATH, "//*[@id=\"pwnedWebsiteBanner\"]/div/div/div[1]/h2")))
        result = self.driver.find_element(By.XPATH, "//*[@id=\"pwnedWebsiteBanner\"]/div/div/div[1]/h2").text

        print("{} : {}".format(email, result))
        self.assertEqual(result, 'Oh no — pwned!')

    def test_second_scenario(self):
        # Second scenario:
        email = "qwerty@somehting.com"
        self.search_bar.clear()
        self.search_bar.send_keys(email)
        self.driver.find_element(By.ID, "searchPwnage").click()

        self.wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id=\"noPwnage\"]/div/div/div[1]/h2")))
        result = self.driver.find_element(By.XPATH, "//*[@id=\"noPwnage\"]/div/div/div[1]/h2").text

        print("{} : {}".format(email, result))
        self.assertEqual(result, 'Good news — no pwnage found!')

    def test_third_scenario(self):
        import time
        report = dict()

        # Third scenario:
        for email in self.emails:

            self.search_bar.clear()
            self.search_bar.send_keys(email)
            self.driver.find_element(By.ID, "searchPwnage").click()

            time.sleep(2)

            pwned = self.driver.find_element(By.XPATH, "//*[@id=\"pwnedWebsiteBanner\"]/div/div/div[1]/h2").text

            if pwned == '':
                no_pwnage = self.driver.find_element(By.XPATH, "//*[@id=\"noPwnage\"]/div/div/div[1]/h2").text

                report[email] = no_pwnage
                continue

            report[email] = pwned

        print(report)
        with open('data.yml', 'w+') as outfile:
            yaml.dump(report, outfile, default_flow_style=False)


if __name__ == '__main__':
    unittest.main()
