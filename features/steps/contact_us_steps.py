from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@given('user visits automationpractice.com Contact Us site')
def step_impl(context):
    context.driver.get(f"{context.BASE_URL}/index.php?controller=contact")


@when('user fills in the form with valid email, message and subject')
def step_impl(context):
    email_input = context.driver.find_element(By.ID, "email")
    message_input = context.driver.find_element(By.ID, "message")
    email_input.send_keys("example@example.com")
    message_input.send_keys("This is a sample message!")
    subject_dropdown = context.driver.find_element(By.ID, "id_contact")
    subject_dropdown.click()
    option = subject_dropdown.find_element(By.XPATH, "//option[2]")
    option.click()
    context.driver.find_element(By.ID, "submitMessage").click()


@then('contact form is sent and user sees success alert')
def step_impl(context):
    alert = WebDriverWait(context.driver, timeout=10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))
    )
    assert alert.text == "Your message has been successfully sent to our team."
