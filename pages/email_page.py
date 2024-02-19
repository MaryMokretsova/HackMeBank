from selene import browser, have, be
import time


class EmailPage:

    def open_bank_page(self):
        browser.open("/#inputForAuth")
        return self

    def assert_name_form(self, value):
        browser.element('.signUpForm').should(have.text(value))
        return self

    def fill_full_name(self, value):
        browser.element('[name="login"]').should(be.blank).type(value)
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

    def assert_placeholder_user_email(self):
        browser.element('.signUpForm__row:nth-child(2) .signUpForm__data:nth-child(2) span:nth-child(2)').should(
            have.text('Электронная почта'))
        return self

    def fill_user_email(self, value):
        browser.element('[type="email"]').clear()
        browser.element('[type="email"]').should(be.blank).type(value)
        return self

    def submit_the_form_with_correct_email(self):
        browser.element('#submitLogin').click()
        time.sleep(1)
        browser.driver.switch_to.alert.accept()
        return self

    def assert_name_modal_window(self, value):
        browser.element('.otp__h1').should(have.text(value))
        return self

    def close_modal_window_security_code(self):
        browser.element('#closeImg').click()
        return self

    def submit_the_form(self):
        browser.element('#submitLogin').click()
        return self

    def assert_message_user_email_without_dots(self):
        browser.element('.signUpForm__row:nth-child(2) .signUpForm__data:nth-child(2) .signUpForm__errText').should(
            have.text('Неправильный формат почты'))
        return self

    def assert_message_user_email_eighty_characters(self):
        browser.element('.signUpForm__row:nth-child(2) .signUpForm__data:nth-child(2) .signUpForm__errText').should(
            have.text('"login" must be a valid email'))
        return self

    def assert_message_user_email_sixty_characters(self):
        browser.element('.signUpForm__row:nth-child(2) .signUpForm__data:nth-child(2) .signUpForm__errText').should(
            have.text('"email" может содержать максимум 50 символов'))
        return self

    def assert_message_user_email_without_dog(self):
        browser.element('.signUpForm__row:nth-child(2) .signUpForm__data:nth-child(2) .signUpForm__errText').should(
            have.text('"email" может содержать максимум 50 символов'))
        return self

    def assert_message_user_email_with_space(self):
        browser.element('.signUpForm__row:nth-child(2) .signUpForm__data:nth-child(2) .signUpForm__errText').should(
            have.text('"email" может содержать максимум 50 символов'))
        return self

    def assert_message_user_email_without_account_name(self):
        browser.element('.signUpForm__row:nth-child(2) .signUpForm__data:nth-child(2) .signUpForm__errText').should(
            have.text('"email" может содержать максимум 50 символов'))
        return self

    def assert_message_user_email_without_subdomain_part(self):
        browser.element('.signUpForm__row:nth-child(2) .signUpForm__data:nth-child(2) .signUpForm__errText').should(
            have.text('"email" может содержать максимум 50 символов'))
        return self

    def assert_message_user_email_with_underscored_subdomain_part(self):
        browser.element('.signUpForm__row:nth-child(2) .signUpForm__data:nth-child(2) .signUpForm__errText').should(
            have.text('"email" может содержать максимум 50 символов'))
        return self


email_page = EmailPage()
