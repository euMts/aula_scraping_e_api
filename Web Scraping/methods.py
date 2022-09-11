from selenium import webdriver

class Utils():
    def __init__(self):
        self.followers = None
        self.get_followers()

    def get_followers(self):
        return_content = {"status": "", "followers": "", "message": ""}
        try:
            driver = webdriver.Firefox()
            driver.get("https://matheus-eduardo.com.br")
            followers_xpath = "//section[@id='hero']/p[2]"
            followers_count = driver.find_element_by_xpath(followers_xpath).text.split()[0]
            driver.close()
            return_content["status"] = "Ok"
            return_content["followers"] = followers_count
            return_content["message"] = ""
            self.followers = return_content
        except Exception as e:
            driver.close()
            return_content["status"] = "Error"
            return_content["message"] = e
            self.followers = return_content

if __name__ == "__main__":
    my_class = Utils()
    followers = my_class.followers["followers"]
    print(f"Followers count = {followers}")