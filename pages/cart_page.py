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

    def assert_name_modal_window(self, value):
        browser.element('.otp__h1').should(have.text(value))
        return self

    def input_modal_window(self):
        security_code=browser.element('.otp__inputs').all('#inputForAuth')
        security_code[0].type('1')
        security_code[1].type('2')
        security_code[2].type('3')
        security_code[3].type('4')

        time.sleep(2)
        return self

    def submit_modal_window(self):
        browser.element('#modalForAuth').click()
        return self

    def assert_answer_modal_window(self, value):
        browser.element('.input_area .signUpForm__errText').should(have.text(value))
        return self


cart_page = CartPage()
