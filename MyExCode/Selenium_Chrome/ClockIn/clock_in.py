from selenium import webdriver
from datetime import datetime
import configparser
import schedule
import time
import os


config = configparser.ConfigParser()
config.read(os.path.dirname(__file__) + '/config.ini', encoding='utf-8')


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
    # driver.find_element_by_xpath(config.get('data', 'SUBMIT_X_PATH')).click()
    print(f'{name}: {datetime.now()} 打卡')
    time.sleep(10)
    driver.close()


def getNameInfo(data: str) -> list[list]:
    data = data.split(',')
    return [i.split(':') for i in data]


def shitf_m_on(week: str):
    for info in getNameInfo(config.get('data', 'NAME')):
        name = info[0]
        shift = info[1]
        week_rest = info[2]
        if shift == '早班':
            if week not in week_rest:
                return submitFrom(name, config.get('data', 'SHIFT_M_ON_X_PATH'))
            else:
                pass
        else:
            pass


def shitf_m_off(week: str):
    for info in getNameInfo(config.get('data', 'NAME')):
        name = info[0]
        shift = info[1]
        week_rest = info[2]
        if shift == '早班':
            if week not in week_rest:
                return submitFrom(name, config.get('data', 'SHIFT_M_OFF_X_PATH'))
            else:
                pass
        else:
            pass


def shitf_n_on(week: str):
    for info in getNameInfo(config.get('data', 'NAME')):
        name = info[0]
        shift = info[1]
        week_rest = info[2]
        if shift == '中班':
            if week not in week_rest:
                return submitFrom(name, config.get('data', 'SHIFT_N_ON_X_PATH'))
            else:
                pass
        else:
            pass


def shitf_n_off(week: str):
    for info in getNameInfo(config.get('data', 'NAME')):
        name = info[0]
        shift = info[1]
        week_rest = info[2]
        if shift == '中班':
            if week not in week_rest:
                return submitFrom(name, config.get('data', 'SHIFT_N_OFF_X_PATH'))
            else:
                pass
        else:
            pass


def shitf_g_on(week: str):
    for info in getNameInfo(config.get('data', 'NAME')):
        name = info[0]
        shift = info[1]
        week_rest = info[2]
        if shift == '晚班':
            if week not in week_rest:
                return submitFrom(name, config.get('data', 'SHIFT_G_ON_X_PATH'))
            else:
                pass
        else:
            pass


def shitf_g_off(week: str):
    for info in getNameInfo(config.get('data', 'NAME')):
        name = info[0]
        shift = info[1]
        week_rest = info[2]
        if shift == '晚班':
            if week not in week_rest:
                return submitFrom(name, config.get('data', 'SHIFT_G_OFF_X_PATH'))
            else:
                pass
        else:
            pass


schedule.every().monday.at('07:40').do(shitf_m_on, '1')
schedule.every().monday.at('17:00').do(shitf_m_off, '1')
schedule.every().tuesday.at('07:40').do(shitf_m_on, '2')
schedule.every().tuesday.at('17:00').do(shitf_m_off, '2')
schedule.every().wednesday.at('07:40').do(shitf_m_on, '3')
schedule.every().wednesday.at('17:00').do(shitf_m_off, '3')
schedule.every().thursday.at('07:40').do(shitf_m_on, '4')
schedule.every().thursday.at('17:00').do(shitf_m_off, '4')
schedule.every().friday.at('07:40').do(shitf_m_on, '5')
schedule.every().friday.at('17:00').do(shitf_m_off, '5')
schedule.every().saturday.at('07:40').do(shitf_m_on, '6')
schedule.every().saturday.at('17:00').do(shitf_m_off, '6')
schedule.every().sunday.at('07:40').do(shitf_m_on, '7')
schedule.every().sunday.at('17:00').do(shitf_m_off, '7')

schedule.every().monday.at('15:40').do(shitf_n_on, '1')
schedule.every().tuesday.at('01:00').do(shitf_n_off, '1')
schedule.every().tuesday.at('15:40').do(shitf_n_on, '2')
schedule.every().wednesday.at('01:00').do(shitf_n_off, '2')
schedule.every().wednesday.at('15:40').do(shitf_n_on, '3')
schedule.every().thursday.at('01:00').do(shitf_n_off, '3')
schedule.every().thursday.at('15:40').do(shitf_n_on, '4')
schedule.every().friday.at('01:00').do(shitf_n_off, '4')
schedule.every().friday.at('15:40').do(shitf_n_on, '5')
schedule.every().saturday.at('01:00').do(shitf_n_off, '5')
schedule.every().saturday.at('15:40').do(shitf_n_on, '6')
schedule.every().sunday.at('01:00').do(shitf_n_off, '6')
schedule.every().sunday.at('15:40').do(shitf_n_on, '7')
schedule.every().monday.at('01:00').do(shitf_n_off, '7')

schedule.every().sunday.at('23:40').do(shitf_g_on, '1')
schedule.every().monday.at('09:00').do(shitf_g_off, '1')
schedule.every().monday.at('23:40').do(shitf_g_on, '2')
schedule.every().tuesday.at('09:00').do(shitf_g_off, '2')
schedule.every().tuesday.at('23:40').do(shitf_g_on, '3')
schedule.every().wednesday.at('09:00').do(shitf_g_off, '3')
schedule.every().wednesday.at('23:40').do(shitf_g_on, '4')
schedule.every().thursday.at('09:00').do(shitf_g_off, '4')
schedule.every().thursday.at('23:40').do(shitf_g_on, '5')
schedule.every().friday.at('09:00').do(shitf_g_off, '5')
schedule.every().friday.at('23:40').do(shitf_g_on, '6')
schedule.every().saturday.at('09:00').do(shitf_g_off, '6')
schedule.every().saturday.at('23:40').do(shitf_g_on, '7')
schedule.every().sunday.at('09:00').do(shitf_g_off, '7')

if __name__ == '__main__':
    print('程式執行中\n Ctrl + c 結束程式')
    while True:
        schedule.run_pending()
        time.sleep(1)
