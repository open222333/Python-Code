from selenium import webdriver
import configparser
import schedule
import time
import os


config = configparser.ConfigParser()
config.read(os.path.dirname(__file__) + '/config.ini')

datalist = config.get('data', 'NAME').split(',')
nameDict = {}
for item in datalist:
    itemlist = item.split(':')
    nameDict[itemlist[0]] = itemlist[1]


def submitFrom(name, shift):
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # 在背景執行
    options.add_argument("--incognito")  # 使用無痕模式
    # 設定driver
    driver_path = os.path.dirname(
        __file__) + '/' + config.get('data', 'DRIVER')
    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    driver.get(config.get('data', 'FORM_URL'))
    driver.find_element_by_xpath(config.get(
        'data', 'NAME_X_PATH')).send_keys(name)
    driver.find_element_by_xpath(shift).click()
    driver.find_element_by_xpath(config.get('data', 'SUBMIT_X_PATH')).click()
    driver.close()


def shitf_m_on():
    return submitFrom(name, config.get('data', 'SHIFT_M_ON_X_PATH'))


def shitf_m_off():
    return submitFrom(name, config.get('data', 'SHIFT_M_OFF_X_PATH'))


def shitf_n_on():
    return submitFrom(name, config.get('data', 'SHIFT_N_ON_X_PATH'))


def shitf_n_off():
    return submitFrom(name, config.get('data', 'SHIFT_N_OFF_X_PATH'))


def shitf_g_on():
    return submitFrom(name, config.get('data', 'SHIFT_G_ON_X_PATH'))


def shitf_g_off():
    return submitFrom(name, config.get('data', 'SHIFT_G_OFF_X_PATH'))


for name in nameDict.keys():
    shift = nameDict[name]
    if shift == '早班':
        schedule.every().day.at('7:40').do(shitf_m_on)
        schedule.every().day.at('17:00').do(shitf_m_off)
    elif shift == '中班':
        schedule.every().day.at('15:40').do(shitf_n_on)
        schedule.every().day.at('1:00').do(shitf_n_off)
    elif shift == '晚班':
        schedule.every().day.at('0:40').do(shitf_g_on)
        schedule.every().day.at('9:00').do(shitf_g_off)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
