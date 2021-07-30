from selenium import webdriver
import configparser
import schedule
import time
import os


config = configparser.ConfigParser()
config.read(os.path.dirname(__file__) + '/config.ini')


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


datalist = config.get('data', 'NAME').split(',')
nameDict = {}
for item in datalist:
    itemlist = item.split(':')
    temp = itemlist[1].split('(')
    temp[1] = temp[1].replace(')', '')
    nameDict[itemlist[0]] = temp

print(nameDict)

for name in nameDict.keys():
    shift = nameDict[name][0]
    week_rest = nameDict[name][1]
    if shift == '早班':
        if '1' not in week_rest:
            schedule.every().monday.at('7:40').do(shitf_m_on)
            schedule.every().monday.at('17:00').do(shitf_m_off)
        elif '2' not in week_rest:
            schedule.every().tuesday.at('7:40').do(shitf_m_on)
            schedule.every().tuesday.at('17:00').do(shitf_m_off)
        elif '3' not in week_rest:
            schedule.every().wednesday.at('7:40').do(shitf_m_on)
            schedule.every().wednesday.at('17:00').do(shitf_m_off)
        elif '4' not in week_rest:
            schedule.every().thursday.at('7:40').do(shitf_m_on)
            schedule.every().thursday.at('17:00').do(shitf_m_off)
        elif '5' not in week_rest:
            schedule.every().friday.at('7:40').do(shitf_m_on)
            schedule.every().friday.at('17:00').do(shitf_m_off)
        elif '6' not in week_rest:
            schedule.every().saturday.at('7:40').do(shitf_m_on)
            schedule.every().saturday.at('17:00').do(shitf_m_off)
        elif '7' not in week_rest:
            schedule.every().sunday.at('7:40').do(shitf_m_on)
            schedule.every().sunday.at('17:00').do(shitf_m_off)
    elif shift == '中班':
        if '1' not in week_rest:
            schedule.every().monday.at('15:40').do(shitf_n_on)
            schedule.every().monday.at('1:00').do(shitf_n_off)
        elif '2' not in week_rest:
            schedule.every().tuesday.at('15:40').do(shitf_n_on)
            schedule.every().tuesday.at('1:00').do(shitf_n_off)
        elif '3' not in week_rest:
            schedule.every().wednesday.at('15:40').do(shitf_n_on)
            schedule.every().wednesday.at('1:00').do(shitf_n_off)
        elif '4' not in week_rest:
            schedule.every().thursday.at('15:40').do(shitf_n_on)
            schedule.every().thursday.at('1:00').do(shitf_n_off)
        elif '5' not in week_rest:
            schedule.every().friday.at('15:40').do(shitf_n_on)
            schedule.every().friday.at('1:00').do(shitf_n_off)
        elif '6' not in week_rest:
            schedule.every().saturday.at('15:40').do(shitf_n_on)
            schedule.every().saturday.at('1:00').do(shitf_n_off)
        elif '7' not in week_rest:
            schedule.every().sunday.at('15:40').do(shitf_n_on)
            schedule.every().sunday.at('1:00').do(shitf_n_off)
    elif shift == '晚班':
        if '1' not in week_rest:
            schedule.every().monday.at('0:40').do(shitf_g_on)
            schedule.every().monday.at('9:00').do(shitf_g_off)
        elif '2' not in week_rest:
            schedule.every().tuesday.at('0:40').do(shitf_g_on)
            schedule.every().tuesday.at('9:00').do(shitf_g_off)
        elif '3' not in week_rest:
            schedule.every().wednesday.at('0:40').do(shitf_g_on)
            schedule.every().wednesday.at('9:00').do(shitf_g_off)
        elif '4' not in week_rest:
            schedule.every().thursday.at('0:40').do(shitf_g_on)
            schedule.every().thursday.at('9:00').do(shitf_g_off)
        elif '5' not in week_rest:
            schedule.every().friday.at('0:40').do(shitf_g_on)
            schedule.every().friday.at('9:00').do(shitf_g_off)
        elif '6' not in week_rest:
            schedule.every().saturday.at('0:40').do(shitf_g_on)
            schedule.every().saturday.at('9:00').do(shitf_g_off)
        elif '7' not in week_rest:
            schedule.every().sunday.at('0:40').do(shitf_g_on)
            schedule.every().sunday.at('9:00').do(shitf_g_off)


if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
