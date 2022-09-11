from selenium import webdriver
from selenium.webdriver.common.alert import Alert 

class Utils():
    def __init__(self, name: str, email: str, message: str):
        self.name = name
        self.email = email
        self.message = message
        self.return_content = {"status": "", "message": ""}
        self.__send_form()

    def __send_form(self):
        try:
            driver = webdriver.Firefox()
            driver.get("https://matheus-eduardo.com.br/contact")
            name_xpath = "//input[@id='name']"
            email_xpath = "//input[@id='email']"
            message_xpath = "//textarea[@id='message']"
            send_button_xpath = "//button[@type='submit'][contains(text(), 'Send')]"
            driver.find_element_by_xpath(name_xpath).send_keys(self.name)
            driver.find_element_by_xpath(email_xpath).send_keys(self.email)
            driver.find_element_by_xpath(message_xpath).send_keys(self.message)
            driver.find_element_by_xpath(send_button_xpath).click()
            alert = Alert(driver)
            alert_message = alert.text
            alert.accept()
            driver.close()
            self.return_content["status"] = "Ok"
            self.return_content["message"] = str(alert_message)
        except Exception as e:
            driver.close()
            self.return_content["status"] = "Error"
            self.return_content["message"] = e

if __name__ == "__main__":
    my_class = Utils("nome", "email", "mensagem")
    print(my_class.return_content)