from lib2to3.pgen2 import driver
from selenium import webdriver

path = 'C:/Users/Abdelfatah/Downloads/Compressed/chromedriver.exe'

driver = webdriver.Chrome(path)

driver.get("https://techwithtim.net")

