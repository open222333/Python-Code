from selenium import webdriver
import configparser
import os


config = configparser.ConfigParser()
config.read(os.path.dirname(__file__) + '/config.ini')
driver_path = os.path.dirname(__file__) + '/' + config.get('data', 'DRIVER')

def submitFrom(shift):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 在背景執行
    options.add_argument("--incognito")  # 使用無痕模式
    # 設定driver
    driver = webdriver.Chrome(driver_path)
    driver.get(config.get('data', 'FORM_URL'))
    driver.find_element_by_xpath(config.get(
        'data', 'NAME_X_PATH')).send_keys(config.get('data', 'NAME'))
    driver.find_element_by_xpath(shift).click()
    # driver.find_element_by_xpath(config.get('data', 'SUBMIT_X_PATH')).click()
    driver.close()


if config.get('data', 'SHIFT') == '早班' and config.get('data', 'SHIFT_') == '上班':
    submitFrom(config.get('data', 'SHIFT_M_ON_X_PATH'))
elif config.get('data', 'SHIFT') == '早班' and config.get('data', 'SHIFT_') == '下班':
    submitFrom(config.get('data', 'SHIFT_M_OFF_X_PATH'))
elif config.get('data', 'SHIFT') == '中班' and config.get('data', 'SHIFT_') == '上班':
    submitFrom(config.get('data', 'SHIFT_N_ON_X_PATH'))
elif config.get('data', 'SHIFT') == '中班' and config.get('data', 'SHIFT_') == '下班':
    submitFrom(config.get('data', 'SHIFT_N_OFF_X_PATH'))
elif config.get('data', 'SHIFT') == '晚班' and config.get('data', 'SHIFT_') == '上班':
    submitFrom(config.get('data', 'SHIFT_G_ON_X_PATH'))
elif config.get('data', 'SHIFT') == '晚班' and config.get('data', 'SHIFT_') == '下班':
    submitFrom(config.get('data', 'SHIFT_G_OFF_X_PATH'))
