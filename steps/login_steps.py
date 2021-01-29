from behave import given, when, then
import time
from selenium.common.exceptions import ElementClickInterceptedException


@given('user is on Orange TV Go website')
def step_start_page(context):
    context.driver.get('https://tvgo.orange.pl/')
    politics = context.driver.find_element_by_class_name('btn-accept')

    if politics.is_displayed():
        politics.click()


@when('user fills valid username {username} and valid password {password} and submits it')
def step_set_login_in(context, username, password):
    context.driver.find_element_by_css_selector('div.btn.r-16').click()
    context.driver.find_element_by_name('username').send_keys(username)
    context.driver.find_element_by_name('password').send_keys(password)
    context.driver.find_element_by_xpath('//html/body/div/div/div/div/form/div/div/div[5]/label').click()
    context.driver.find_element_by_class_name('full-width').click()


@then('user can see my zone')
def step_valid_login(context):
    time.sleep(1)
    context.driver.find_element_by_class_name('profile-img-container').click()

    parential = context.driver.find_element_by_class_name('b-16.maskedText')
    if parential.is_displayed():
        context.driver.find_element_by_class_name('b-16.maskedText').send_keys('1111')
        context.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[3]/div[2]/span').click()
    time.sleep(4)
    context.driver.save_screenshot("screenshot-login.png")
    assert context.driver.find_element_by_class_name('icon-cloud-recording')


@when('user fills invalid username {invalidusername} and/or invalid password {invalidpassword} and submits it')
def step_set_login_in(context, invalidusername, invalidpassword):
    context.driver.find_element_by_css_selector('div.btn.r-16').click()
    context.driver.find_element_by_name('username').send_keys(invalidusername)
    context.driver.find_element_by_name('password').send_keys(invalidpassword)
    context.driver.find_element_by_xpath('//html/body/div/div/div/div/form/div/div/div[5]/label').click()
    context.driver.find_element_by_class_name('full-width').click()


@then('User can see alert about invalid data')
def step_invalid_login(context):
    try:
        alert_content = context.driver.find_element_by_class_name("alert.alert-danger")

        assert alert_content.is_displayed()
        print("Invalid login data")
        context.driver.save_screenshot("screenshot-invalidlogin.png")
    except:
        print('Alert not found')


@then('User logout')
def step_logout(context):
    time.sleep(1)
    context.driver.find_element_by_class_name('profile-img-container').click()
    parential = context.driver.find_element_by_class_name('b-16.maskedText')
    if parential.is_displayed():
        context.driver.find_element_by_class_name('b-16.maskedText').send_keys('1111')
        context.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[3]/div[2]/span').click()
    time.sleep(4)
    context.driver.save_screenshot("screenshot-login.png")
    context.driver.find_element_by_class_name('profile-img.null').click()
    context.driver.find_element_by_class_name('dropdown-item.logout').click()
    time.sleep(3)
    context.driver.save_screenshot("screenshot-logout.png")
    assert context.driver.find_element_by_css_selector('div.btn.r-16')
