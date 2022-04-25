# Import bibliotek
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



imie = "Agata"
nazwisko = "Kwiat"
email = "agata@oo.pl"
telefon = "000000000"
haslo = "kotojelen"
zle_haslo = "ul"

class CCCRegistrationPage:
    Cookies = "//*[@id='cookiesModal']/div/div/div/div/div[1]/span"
    ZalogujButton = "/html/body/div[2]/div[4]/div/div[3]/div/div/div[3]/div/ul/li[3]/div/a/span[2]"
    FirstNameID = "enp_customer_registration_form_type_address_firstName"
    LastNameID = "enp_customer_registration_form_type_address_lastName"
    EmailID = "enp_customer_registration_form_type_email"
    NumberID = "enp_customer_registration_form_type_mobileNumber"
    FirstPasswordID = "enp_customer_registration_form_type_plainPassword_first"
    SecondPasswordID = "enp_customer_registration_form_type_plainPassword_second"
    AcceptButton = "//div[@class='a-form_label  ']"
    SubmitButton = "//input[@class='c-btn is-primary is-submitBtn']"
    AcceptButtonError = "/html/body/div[2]/div[8]/div/div[2]/div[2]/div/div[2]/form/div[7]/div/label/div[2]"
    FirstNameError = "/html/body/div[2]/div[8]/div/div[2]/div[2]/div/div[2]/form/div[1]/div/div[2]"
    LastNameError = "/html/body/div[2]/div[8]/div/div[2]/div[2]/div/div[2]/form/div[2]/div/div[2]"
    EmailError = "/html/body/div[2]/div[8]/div/div[2]/div[2]/div/div[2]/form/div[3]/div/div[2]"
    WrongPasswordError = "/html/body/div[2]/div[8]/div/div[2]/div[2]/div/div[2]/form/div[5]/div/div[3]"
    PasswordError = "/html/body/div[2]/div[8]/div/div[2]/div[2]/div/div[2]/form/div[6]/div/div[2]"






class BaseTestHome(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://ccc.eu/pl/")
        self.driver.implicitly_wait(15)

    def test_checkRegistrationPage(self):
        #1.2.1
        #Test logowania bez zaznaczenia pola "akceptuj regulamin"

        driver = self.driver
        driver.find_element(By.XPATH, CCCRegistrationPage.Cookies) .click()
        driver.find_element(By.XPATH,CCCRegistrationPage.ZalogujButton).click()
        driver.find_element(By.ID, CCCRegistrationPage.FirstNameID).click()
        driver.find_element(By.ID, CCCRegistrationPage.FirstNameID).send_keys(imie)
        driver.find_element(By.ID, CCCRegistrationPage.LastNameID).send_keys(nazwisko)
        driver.find_element(By.ID, CCCRegistrationPage.EmailID ).send_keys(email)
        driver.find_element(By.ID, CCCRegistrationPage.NumberID).click()
        driver.find_element(By.ID, CCCRegistrationPage.NumberID).send_keys(telefon)
        driver.find_element(By.ID, CCCRegistrationPage.FirstPasswordID).send_keys(haslo)
        driver.find_element(By.ID, CCCRegistrationPage.SecondPasswordID).send_keys(haslo)
        sleep(10)
        #Pominięcie akceptacji regulaminu
        driver.find_element(By.XPATH, CCCRegistrationPage.SubmitButton).click()
        error_info = driver.find_element(By.XPATH, CCCRegistrationPage.AcceptButtonError) .text
        self.assertEqual("To pole jest wymagane", error_info)
        sleep(20)



    def test_RegistrationPageCheckFirstName(self):
        #1.2.2
        #Test logowania bez wpisania imienia

        driver = self.driver
        driver.find_element(By.XPATH, CCCRegistrationPage.Cookies).click()
        driver.find_element(By.XPATH, CCCRegistrationPage.ZalogujButton).click()
        #Pominięcie wpisania pola imię
        driver.find_element(By.ID, CCCRegistrationPage.LastNameID).send_keys(nazwisko)
        driver.find_element(By.ID, CCCRegistrationPage.EmailID).send_keys(email)
        driver.find_element(By.ID, CCCRegistrationPage.NumberID).click()
        driver.find_element(By.ID, CCCRegistrationPage.NumberID).send_keys(telefon)
        driver.find_element(By.ID, CCCRegistrationPage.FirstPasswordID).send_keys(haslo)
        driver.find_element(By.ID, CCCRegistrationPage.SecondPasswordID).send_keys(haslo)
        sleep(10)
        driver.find_element(By.XPATH, CCCRegistrationPage.AcceptButton).click()
        sleep(10)
        driver.find_element(By.XPATH, CCCRegistrationPage.SubmitButton).click()
        sleep(5)
        error_info = driver.find_element(By.XPATH, CCCRegistrationPage.FirstNameError).text
        self.assertEqual("To pole jest wymagane", error_info)
        sleep(5)



    def test_RegistrationPageCheckLastName(self):
        #1.2.3
        #Test logowania bez wpisania nazwiska

        driver = self.driver
        driver.find_element(By.XPATH, CCCRegistrationPage.Cookies).click()
        driver.find_element(By.XPATH, CCCRegistrationPage.ZalogujButton).click()
        driver.find_element(By.ID, CCCRegistrationPage.FirstNameID).click()
        driver.find_element(By.ID, CCCRegistrationPage.FirstNameID).send_keys(imie)
        #Pominięcie wpisania nazwiska
        driver.find_element(By.ID, CCCRegistrationPage.EmailID).send_keys(email)
        driver.find_element(By.ID, CCCRegistrationPage.NumberID).click()
        driver.find_element(By.ID, CCCRegistrationPage.NumberID).send_keys(telefon)
        driver.find_element(By.ID, CCCRegistrationPage.FirstPasswordID).send_keys(haslo)
        driver.find_element(By.ID, CCCRegistrationPage.SecondPasswordID).send_keys(haslo)
        sleep(10)
        driver.find_element(By.XPATH, CCCRegistrationPage.AcceptButton).click()
        sleep(10)
        driver.find_element(By.XPATH, CCCRegistrationPage.SubmitButton).click()
        sleep(10)
        error_info = driver.find_element(By.XPATH,CCCRegistrationPage.LastNameError).text
        self.assertEqual("To pole jest wymagane", error_info)
        sleep(5)



    def test_RegistrationPageCheckEmail(self):
        #1.2.4
        #Test logowania bez wpisania e-maila

        driver = self.driver
        driver.find_element(By.XPATH, CCCRegistrationPage.Cookies).click()
        driver.find_element(By.XPATH, CCCRegistrationPage.ZalogujButton).click()
        driver.find_element(By.ID, CCCRegistrationPage.FirstNameID).click()
        driver.find_element(By.ID, CCCRegistrationPage.FirstNameID).send_keys(imie)
        driver.find_element(By.ID, CCCRegistrationPage.LastNameID).send_keys(nazwisko)
        #Pominięcie wpisania adresu e-mail
        driver.find_element(By.ID, CCCRegistrationPage.NumberID).click()
        driver.find_element(By.ID, CCCRegistrationPage.NumberID).send_keys(telefon)
        driver.find_element(By.ID, CCCRegistrationPage.FirstPasswordID).send_keys(haslo)
        driver.find_element(By.ID, CCCRegistrationPage.SecondPasswordID).send_keys(haslo)
        sleep(10)
        driver.find_element(By.XPATH, CCCRegistrationPage.AcceptButton).click()
        sleep(10)
        driver.find_element(By.XPATH, CCCRegistrationPage.SubmitButton).click()
        sleep(10)
        error_info = driver.find_element(By.XPATH, CCCRegistrationPage.EmailError) .text
        self.assertEqual("To pole jest wymagane", error_info)
        sleep(5)



    def test_RegistrationPageCheckShortPassword(self):
        #1.2.5
        #Test logowania przy użyciu za któtkiego hasła

        driver = self.driver
        driver.find_element(By.XPATH, CCCRegistrationPage.Cookies).click()
        driver.find_element(By.XPATH, CCCRegistrationPage.ZalogujButton).click()
        driver.find_element(By.ID, CCCRegistrationPage.FirstNameID).click()
        driver.find_element(By.ID, CCCRegistrationPage.FirstNameID).send_keys(imie)
        driver.find_element(By.ID, CCCRegistrationPage.LastNameID).send_keys(nazwisko)
        driver.find_element(By.ID, CCCRegistrationPage.EmailID).send_keys(email)
        driver.find_element(By.ID, CCCRegistrationPage.NumberID).click()
        driver.find_element(By.ID, CCCRegistrationPage.NumberID).send_keys(telefon)
        driver.find_element(By.ID, CCCRegistrationPage.FirstPasswordID).send_keys(zle_haslo)
        driver.find_element(By.ID, CCCRegistrationPage.SecondPasswordID).send_keys(zle_haslo)
        sleep(10)
        driver.find_element(By.XPATH, CCCRegistrationPage.AcceptButton).click()
        sleep(10)
        driver.find_element(By.XPATH, CCCRegistrationPage.SubmitButton).click()
        sleep(10)
        error_info = driver.find_element(By.XPATH, CCCRegistrationPage.WrongPasswordError).text
        self.assertEqual("Hasło musi składać się z co najmniej 8 znaków", error_info)
        sleep(5)



    def test_RegistrationPageCheckPassword(self):
        #1.2.6
        #Test logowania przy wpisaniu dwóch różnych haseł

        driver = self.driver
        driver.find_element(By.XPATH, CCCRegistrationPage.Cookies).click()
        driver.find_element(By.XPATH, CCCRegistrationPage.ZalogujButton).click()
        driver.find_element(By.ID, CCCRegistrationPage.FirstNameID).click()
        driver.find_element(By.ID, CCCRegistrationPage.FirstNameID).send_keys(imie)
        driver.find_element(By.ID, CCCRegistrationPage.LastNameID).send_keys(nazwisko)
        driver.find_element(By.ID, CCCRegistrationPage.EmailID).send_keys(email)
        driver.find_element(By.ID, CCCRegistrationPage.NumberID).click()
        driver.find_element(By.ID, CCCRegistrationPage.NumberID).send_keys(telefon)
        driver.find_element(By.ID, CCCRegistrationPage.FirstPasswordID).send_keys(haslo)
        driver.find_element(By.ID, CCCRegistrationPage.SecondPasswordID).send_keys(zle_haslo)
        sleep(10)
        driver.find_element(By.XPATH, CCCRegistrationPage.AcceptButton).click()
        sleep(10)
        driver.find_element(By.XPATH, CCCRegistrationPage.SubmitButton).click()
        sleep(10)
        error_info = driver.find_element(By.XPATH,CCCRegistrationPage.PasswordError).text
        self.assertEqual("Podane hasła nie są takie same", error_info)
        sleep(5)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
