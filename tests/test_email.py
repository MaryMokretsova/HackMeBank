
import allure
from pages.email_page import email_page
from test_data.user_data import VALID_CREDENTIALS, VALID_REPEAT_CREDENTIALS


class TestEmail:

    @allure.title("Application form to receive a card with check field email")
    def test_form_to_receive_cart(self):
        with allure.step("Open bank"):
            email_page.open_bank_page()
        with allure.step("Assert name form application"):
            email_page.assert_name_form('Карта HackMeBank уже сегодня')
        with allure.step("Input user full name"):
            email_page.fill_full_name('Ivanov Ivan Ivanovich')
        with allure.step("Input user phone"):
            email_page.fill_user_phone_number('89066507070')
        with allure.step("Input password"):
            email_page.fill_password(VALID_CREDENTIALS.password)
        with allure.step("Input repeat password"):
            email_page.fill_repeat_password(VALID_REPEAT_CREDENTIALS.password)
        with allure.step("Click first checkbox"):
            email_page.first_checkbox()
        with allure.step("Click second checkbox"):
            email_page.second_checkbox()

        with allure.step("Assert tooltip in the field with name email"):
            email_page.assert_placeholder_user_email()

        with allure.step("Input user email starts with the numbers in the account name"):
            email_page.fill_user_email('105cameron@mail.ru')
        with allure.step("Submit the form with correct email"):
            email_page.submit_the_form_with_correct_email()
        with allure.step("Assert name modal window security code"):
            email_page.assert_name_modal_window('Код проверки')
        with allure.step("Close modal window security code"):
            email_page.close_modal_window_security_code()

        with allure.step("Input user email starts with the letters in the account name"):
            email_page.fill_user_email('cameron@mail.ru')
        with allure.step("Submit the form with correct email"):
            email_page.submit_the_form_with_correct_email()
        with allure.step("Assert name modal window security code"):
            email_page.assert_name_modal_window('Код проверки')
        with allure.step("Close modal window security code"):
            email_page.close_modal_window_security_code()

        with allure.step("Input user email ends with the letters in the account name"):
            email_page.fill_user_email('cameron@mail.ru')
        with allure.step("Submit the form with correct email"):
            email_page.submit_the_form_with_correct_email()
        with allure.step("Assert name modal window security code"):
            email_page.assert_name_modal_window('Код проверки')
        with allure.step("Close modal window security code"):
            email_page.close_modal_window_security_code()

        with allure.step("Input user email ends with the numbers in the account name"):
            email_page.fill_user_email('cameron105105@mail.ru')
        with allure.step("Submit the form with correct email"):
            email_page.submit_the_form_with_correct_email()
        with allure.step("Assert name modal window security code"):
            email_page.assert_name_modal_window('Код проверки')
        with allure.step("Close modal window security code"):
            email_page.close_modal_window_security_code()

        with allure.step("Input user email with underscored in the account name"):
            email_page.fill_user_email('c_a_m_e_r_o_n_105@mail.ru')
        with allure.step("Submit the form with correct email"):
            email_page.submit_the_form_with_correct_email()
        with allure.step("Assert name modal window security code"):
            email_page.assert_name_modal_window('Код проверки')
        with allure.step("Close modal window security code"):
            email_page.close_modal_window_security_code()

        with allure.step("Input user email with dots in the account name"):
            email_page.fill_user_email('c.a.m.e.r.o.n.105@mail.ru')
        with allure.step("Submit the form with correct email"):
            email_page.submit_the_form_with_correct_email()
        with allure.step("Assert name modal window security code"):
            email_page.assert_name_modal_window('Код проверки')
        with allure.step("Close modal window security code"):
            email_page.close_modal_window_security_code()

        with allure.step("Input user email with hyphenated in the account name"):
            email_page.fill_user_email('c-a-m-e-r-o-n-105@mail.ru')
        with allure.step("Submit the form with correct email"):
            email_page.submit_the_form_with_correct_email()
        with allure.step("Assert name modal window security code"):
            email_page.assert_name_modal_window('Код проверки')
        with allure.step("Close modal window security code"):
            email_page.close_modal_window_security_code()

        with allure.step("Input user email with uppercase"):
            email_page.fill_user_email('CAMERON105@MAIL.RU')
        with allure.step("Submit the form with correct email"):
            email_page.submit_the_form_with_correct_email()
        with allure.step("Assert name modal window security code"):
            email_page.assert_name_modal_window('Код проверки')
        with allure.step("Close modal window security code"):
            email_page.close_modal_window_security_code()

        with allure.step("Input user email with hyphenated in the subdomain part"):
            email_page.fill_user_email('cameron105@m-a-i-l.ru')
        with allure.step("Submit the form with correct email"):
            email_page.submit_the_form_with_correct_email()
        with allure.step("Assert name modal window security code"):
            email_page.assert_name_modal_window('Код проверки')
        with allure.step("Close modal window security code"):
            email_page.close_modal_window_security_code()

        with allure.step("Input user email with dots in the subdomain part"):
            email_page.fill_user_email('cameron105@m.a.i.l.ru')
        with allure.step("Submit the form with correct email"):
            email_page.submit_the_form_with_correct_email()
        with allure.step("Assert name modal window security code"):
            email_page.assert_name_modal_window('Код проверки')
        with allure.step("Close modal window security code"):
            email_page.close_modal_window_security_code()

        with allure.step("Input user email without dots in the subdomain part"):
            email_page.fill_user_email('cameron105@mailru')
        with allure.step("Submit the form"):
            email_page.submit_the_form()
        with allure.step("Assert message if email without dots in the subdomain part"):
            email_page.assert_message_user_email_without_dots()

        with allure.step("Input exceeding user email length (>80 characters)"):
            email_page.fill_user_email('lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll@nail'
                                       '.com')
        with allure.step("Submit the form"):
            email_page.submit_the_form()
        with allure.step("Assert message if exceeding user email length (>80 characters)"):
            email_page.assert_message_user_email_eighty_characters()

        with allure.step("Input exceeding user email length (>60 characters)"):
            email_page.fill_user_email('lllllllllllllllllllllllllllllllllllllllllllllllllll@nail.com')
        with allure.step("Submit the form"):
            email_page.submit_the_form()
        with allure.step("Assert message if exceeding user email length (>60 characters)"):
            email_page.assert_message_user_email_sixty_characters()

        with allure.step("Input without @ in user email"):
            email_page.fill_user_email('cameron105mail.ru')
        with allure.step("Submit the form"):
            email_page.submit_the_form()
        with allure.step("Assert message if without @ in user email"):
            email_page.assert_message_user_email_without_dog()

        with allure.step("Input user email with spaces in account name"):
            email_page.fill_user_email('c a m e r o n105@mail.ru')
        with allure.step("Submit the form"):
            email_page.submit_the_form()
        with allure.step("Assert message if user email with spaces in account name"):
            email_page.assert_message_user_email_with_space()

        with allure.step("Input user email without an account name"):
            email_page.fill_user_email('@mail.ru')
        with allure.step("Submit the form"):
            email_page.submit_the_form()
        with allure.step("Assert message if user email without an account name"):
            email_page.assert_message_user_email_without_account_name()

        with allure.step("Input user email without subdomain part"):
            email_page.fill_user_email('cameron105@.ru')
        with allure.step("Submit the form"):
            email_page.submit_the_form()
        with allure.step("Assert message if user email without subdomain part"):
            email_page.assert_message_user_email_without_subdomain_part()

        with allure.step("Input user email with underscored in the subdomain part"):
            email_page.fill_user_email('cameron105@m_a_i_l.ru')
        with allure.step("Submit the form"):
            email_page.submit_the_form()
        with allure.step("Assert message if user email with underscored in the subdomain part"):
            email_page.assert_message_user_email_with_underscored_subdomain_part()

