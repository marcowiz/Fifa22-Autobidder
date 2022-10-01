import selenium




driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
driver.get("https://www.futbin.com/players?page=1&position=CB&nation=18&order=asc&sort=ps_price&version=gold")



def check_for_results():
        parentOfTbody = driver.find_element(By.ID, "repTb")
        tbody =  parentOfTbody.find_element(By.XPATH, "/tbody")
        #tbody = self.driver.find_element_by_xpath("/html/body/div[9]/div[2]/div[5]/div[3]/table/tbody")
        stats = tbody.find_elements(By.XPATH, './tr')

        for row in stats:
            test = row.text
            if test == "No Results":
                return False
        return True

print(check_for_results)