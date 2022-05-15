from selenium import webdriver

PATH = r"C:\Users\nafiz\Downloads\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")