from selenium.webdriver import Chrome, ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.google.com/")
