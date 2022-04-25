# Import bibliotek
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


#Zmienne

email = "agata@oo.pl"
name = "Agata"
lastname = "Kwiat"
valueday = "10"
valuemonth = "10"
valueyear = "1990"
password = "kotojelen"
address = "Kwiatowa 10"
city = "Warszawa"
postalcode = "12345"
phone = "000000000"
alias = "my alias"

class automationpracticeHomePage:

    ZakladkaDresses = "//*[@id='block_top_menu']/ul/li[2]/a"
    Dress1 = "//*[@id='center_column']/ul/li[1]/div"
    Dress1AddToCart = "//*[@id='center_column']/ul/li[1]/div/div[2]/div[2]/a[1]/span"
    ContinueShopping = "//*[@id='layer_cart']/div[1]/div[2]/div[4]/span/span"
    Dress2 = "//*[@id='center_column']/ul/li[5]/div"
    Dress2AddToCart = "//*[@id='center_column']/ul/li[5]/div/div[2]/div[2]/a[1]"
    ProceedToCheckout = "//*[@id='layer_cart']/div[1]/div[2]/div[4]/a"
    ProceedToCheckout2 = "//*[@id='center_column']/p[2]/a[1]"
    CreateAnAccount = "//*[@id='SubmitCreate']"
    ErrorMessage = "//*[@id='center_column']/div"
    ErrorMessage2 = '//div[@class="alert alert-danger"]/ol/li'
    EmailID = "email_create"
    GenderID = "id_gender2"
    LastNameID = "customer_lastname"
    PasswordID = "passwd"
    DayID = "days"
    MonthID = "months"
    YearID = "years"
    AddressID = "address1"
    CityID = "city"
    PostCodeID = "postcode"
    StateID = "id_state"
    MobilePhoneID = "phone_mobile"
    AliasID = "alias"
    SubmitAccountButton = "submitAccount"


class BaseTestHome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com")
        self.driver.implicitly_wait(15)

    def test_checkCartPage(self):
        driver = self.driver
        #1.Kliknięcie zakładki DRESSES
        driver.find_element(By.XPATH, automationpracticeHomePage.ZakladkaDresses) .click()
        #2.Kliknięcie pierwszej sukienki
        driver.find_element(By.XPATH, automationpracticeHomePage.Dress1) .click()
        #3.Dodanie pierwszej sukienki do koszyka
        driver.find_element(By.XPATH, automationpracticeHomePage.Dress1AddToCart) .click()
        #4.Czekanie na pojawienie okna i kliknięcie buttonu kontynuuj zakupy
        sleep(3)
        driver.find_element(By.XPATH, automationpracticeHomePage.ContinueShopping) .click()
        #5.Kliknięcie drugiej sukienki
        driver.find_element(By.XPATH, automationpracticeHomePage.Dress2) .location_once_scrolled_into_view
        #6.Dodanie drugiej sukienki do koszyka
        driver.find_element(By.XPATH, automationpracticeHomePage.Dress2AddToCart) .click()
        #7.Kliknięcie buttonu do podsumowania
        driver.find_element(By.XPATH, automationpracticeHomePage.ProceedToCheckout) .click()
        sleep(5)
        #8.Kliknij utwórz konto
        self.driver.find_element(By.XPATH, automationpracticeHomePage.ProceedToCheckout2) .click()
        sleep(5)
        #8.Wpisanie adresu e-mail
        email_input = self.driver.find_element(By.ID, automationpracticeHomePage.EmailID)
        email_input.send_keys(email)
        self.driver.find_element(By.XPATH, automationpracticeHomePage.CreateAnAccount) .click()
        #9.Wybierz plec
        self.driver.find_element(By.ID, automationpracticeHomePage.GenderID) .click()
        sleep(2)
        #10.Wpisanie nazwiska
        lastname_input = driver.find_element(By.ID, automationpracticeHomePage.LastNameID)
        lastname_input.send_keys(lastname)
        sleep(1)
        #11.Wpisanie hasła
        password_input = driver.find_element(By.ID, automationpracticeHomePage.PasswordID)
        password_input.send_keys(password)
        #12.Wybór daty urodzenia
        day = Select(driver.find_element(By.ID, automationpracticeHomePage.DayID))
        day.select_by_value(valueday)
        month = Select(driver.find_element(By.ID, automationpracticeHomePage.MonthID))
        month.select_by_value(valuemonth)
        year = Select(driver.find_element(By.ID, automationpracticeHomePage.YearID))
        year.select_by_value(valueyear)
        sleep(5)
        #13.Wpisanie adresu
        address_input = driver.find_element(By.ID, automationpracticeHomePage.AddressID)
        address_input.send_keys(address)
        #14.Wpisanie miasta
        city_input = driver.find_element(By.ID, automationpracticeHomePage.CityID)
        city_input.send_keys(city)
        #15.Wpisanie kodu pocztowego
        code_input = driver.find_element(By.ID, automationpracticeHomePage.PostCodeID)
        code_input.send_keys(postalcode)
        sleep(3)
        #16.Wybór stanu
        state = Select(driver.find_element(By.ID, automationpracticeHomePage.StateID))
        state.select_by_value('2')
        #17.Wpisanie numer telefonu
        password_input = driver.find_element(By.ID, automationpracticeHomePage.MobilePhoneID)
        password_input.send_keys(phone)
        #18.Wpisanie alias adresu
        alias_input = driver.find_element(By.ID, automationpracticeHomePage.AliasID)
        alias_input.clear()
        alias_input.send_keys(alias)
        #19.Kliknięcie przycisku "Register"
        driver.find_element(By.ID, automationpracticeHomePage.SubmitAccountButton).click()
        sleep(5)
        #Sprawdzanie ileości błędów
        error_number_info = driver.find_element(By.XPATH, automationpracticeHomePage.ErrorMessage).text
        self.assertEqual("There is 1 error\nfirstname is required.", error_number_info)

        error_messages = driver.find_elements(By.XPATH, automationpracticeHomePage.ErrorMessage2)
        # Sprawdzanie, czy jest tylko jedna informacja o błedzie
        self.assertEqual(1, len(error_messages))
        # Sprawdzanie treści tej informacji
        self.assertEqual("firstname is required.", error_messages[0].text)
        sleep(3)


    def tearDown(self):
         self.driver.quit()

if __name__ == "__main__":
     unittest.main()