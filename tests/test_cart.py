import allure
from pages.cart_page import cart_page
from test_data.user_data import VALID_CREDENTIALS, VALID_REPEAT_CREDENTIALS


class TestCart:

    @allure.title("Application form to receive a card")
    def test_form_to_receive_cart(self):
        with allure.step("Open bank"):
            cart_page.open_bank_page()
        with allure.step("Assert name form application"):
            cart_page.assert_name_form('Карта HackMeBank уже сегодня')
        with allure.step("Input user full name"):
            cart_page.fill_full_name('Ivanov Ivan Ivanovich')
        with allure.step("Input user email"):
            cart_page.fill_user_email('cameron105@mail.ru')
        with allure.step("Input user phone"):
            cart_page.fill_user_phone_number('1234567890')
        with allure.step("Input password"):
            cart_page.fill_password(VALID_CREDENTIALS.password)
        with allure.step("Input repeat password"):
            cart_page.fill_repeat_password(VALID_REPEAT_CREDENTIALS.password)
        with allure.step("Click first checkbox"):
            cart_page.first_checkbox()
        with allure.step("Click second checkbox"):
            cart_page.second_checkbox()
        with allure.step("Submit the form"):
            cart_page.submit_the_form()
