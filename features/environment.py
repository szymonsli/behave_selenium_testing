from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_feature(context, feature):
    context.BASE_URL = "http://automationpractice.com"
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    context.driver.implicitly_wait(2)


def after_feature(context, feature):
    context.driver.quit()
