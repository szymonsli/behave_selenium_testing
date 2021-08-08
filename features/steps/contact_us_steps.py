from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from os import getcwd

img1 = getcwd() + "/features/img/img1.jpg"


@given('user visits automationpractice.com Contact Us site')
def visit_contact_us(context):
    context.driver.get(f"{context.BASE_URL}/index.php?controller=contact")


@when('user fills in the form with valid email, message and subject')
def fill_form_correctly(context):
    email_input = context.driver.find_element(By.ID, "email")
    message_input = context.driver.find_element(By.ID, "message")
    email_input.send_keys("example@example.com")
    message_input.send_keys("This is a sample message!")
    subject_dropdown = context.driver.find_element(By.ID, "id_contact")
    subject_dropdown.click()
    option = subject_dropdown.find_element(By.XPATH, "//option[2]")
    option.click()


@when('clicks submit button')
def click_submit_button(context):
    context.driver.find_element(By.ID, "submitMessage").click()


@when('attach a file')
def attach_file(context):
    file_input = context.driver.find_element(By.ID, "fileUpload")
    file_input.send_keys(img1)


@then('contact form is sent and user sees success alert')
def contact_form_is_sent(context):
    alert = WebDriverWait(context.driver, timeout=10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))
    )
    assert alert.text == "Your message has been successfully sent to our team."
