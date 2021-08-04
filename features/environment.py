from selenium import webdriver


def before_feature(context, feature):
    context.BASE_URL = "http://automationpractice.com"
    context.driver = webdriver.Chrome('./../chromedriver.exe')
    context.driver.maximize_window()
    context.driver.implicitly_wait(2)


def after_feature(context, feature):
    context.driver.quit()
