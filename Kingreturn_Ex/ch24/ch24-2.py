from selenium import webdriver

driverPath = '/opt/homebrew/bin/chromedriver'
browser = webdriver.Firefox(executable_path=driverPath)
print(type(browser))
