from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import urllib.request


class Calculator():
    def __init__(self, equation):
        super().__init__()

        self.url = 'https://www.wolframalpha.com/'
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(
            'C:\\Users\\TymB\\Desktop\\Programs\\chromedriver\\chromedriver.exe', chrome_options=self.options)
        self.equation = equation
        self.plot_error = 0

    def calculate(self):
        self.driver.get(self.url)
        self.input_field = self.driver.find_element(
            By.XPATH, '//*[@id="__next"]/div/div[1]/div/div/div[1]/section/form/div/div/input')
        self.input_field.send_keys(self.equation)
        self.input_field.send_keys(Keys.RETURN)
        time.sleep(5)

        try:
            self.header = self.driver.find_element(
                By.XPATH, '//*[contains(text(), "Differential equation solution")]')
            self.solution_image = self.header.find_element(
                By.XPATH, 'following::img[1]')
            self.solution = self.solution_image.get_attribute('alt')
            solution_url = self.solution_image.get_attribute('src')
            urllib.request.urlretrieve(solution_url, 'solution_img.png')
        except:
            print('No avaliable solution')

        try:
            self.plot1_header = self.driver.find_element(
                By.XPATH, '//*[contains(text(), "Slope field")]')
            self.plot1 = self.plot1_header.find_element(
                By.XPATH, 'following::img[1]')
            plot1_url = self.plot1.get_attribute('src')
            urllib.request.urlretrieve(plot1_url, 'plot1')
        except:
            print('There is no Slope field plot')
            self.plot_error = 1
        try:
            self.plot2_header = self.driver.find_element(
                By.XPATH, '//*[contains(text(), "Plots of sample individual solution")]')
            self.plot2 = self.plot2_header.find_element(
                By.XPATH, 'following::img[1]')
            plot2_url = self.plot2.get_attribute('src')
            urllib.request.urlretrieve(plot2_url, 'plot2')
        except:
            print('There is no Plots of sample individual solution')
            self.plot_error = 2
        try:
            self.plot3_header = self.driver.find_element(
                By.XPATH, '//*[contains(text(), "Sample solution family")]')
            self.plot3 = self.plot3_header.find_element(
                By.XPATH, 'following::img[1]')
            plot3_url = self.plot3.get_attribute('src')
            urllib.request.urlretrieve(plot3_url, 'plot3')
        except:
            print('There is no Sample solution family plot')
            self.plot_error = 3

        self.driver.quit()
        print(self.plot_error)
        return self.solution, self.plot_error
