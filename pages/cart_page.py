from selene import browser, have, be
import time


class CartPage:

    def open_bank_page(self):
        browser.open("/#inputForAuth")
        return self

    def assert_name_form(self, value):
        browser.element('.signUpForm').should(have.text(value))
        return self

    def fill_full_name(self, value):
        browser.element('[name="login"]').should(be.blank).type(value)
        return self

    def fill_user_email(self, value):
        browser.element('[type="email"]').should(be.blank).type(value)
        return self

    def fill_user_phone_number(self, value):
        browser.element('#phoneNumber').should(be.blank).type(value)
        return self

    def fill_password(self, password):
        browser.element('[placeholder="Пароль"]').should(be.blank).type(password)
        return self

    def fill_repeat_password(self, password):
        browser.element('[placeholder="Повторите пароль"]').should(be.blank).type(password)
        return self

    def first_checkbox(self):
        browser.element('.signUpForm__checkoboxItem:nth-child(1)').click()
        return self

    def second_checkbox(self):
        browser.element('.signUpForm__checkoboxItem:nth-child(2)').click()
        return self

    def submit_the_form(self):
        browser.element('#submitLogin').click()
        time.sleep(1)
        browser.driver.switch_to.alert.accept()
        return self

# OK


cart_page = CartPage()
