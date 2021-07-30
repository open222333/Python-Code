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


datalist = config.get('data', 'NAME').split(',')
nameDict = {}
for item in datalist:
    itemlist = item.split(':')
    nameDict[itemlist[0]] = itemlist[1]

for name in nameDict.keys():
    shift = nameDict[name]
    if shift == '早班':
        schedule.every().day.at('7:40').do(
            submitFrom(name, config.get('data', 'SHIFT_M_ON_X_PATH')))
        schedule.every().day.at('17:00').do(
            submitFrom(name, config.get('data', 'SHIFT_M_OFF_X_PATH')))


# if config.get('data', 'SHIFT') == '早班':
#     schedule.every().day.at('7:40').do(
#         submitFrom(config.get('data', 'SHIFT_M_ON_X_PATH')))
#     schedule.every().day.at('17:00').do(
#         submitFrom(config.get('data', 'SHIFT_M_OFF_X_PATH')))
# elif config.get('data', 'SHIFT') == '中班':
#     schedule.every().day.at('15:40').do(
#         submitFrom(config.get('data', 'SHIFT_N_ON_X_PATH')))
#     schedule.every().day.at('1:00').do(
#         submitFrom(config.get('data', 'SHIFT_N_OFF_X_PATH')))
# elif config.get('data', 'SHIFT') == '晚班':
#     schedule.every().day.at('0:40').do(
#         submitFrom(config.get('data', 'SHIFT_G_ON_X_PATH')))
#     schedule.every().day.at('9:00').do(
#         submitFrom(config.get('data', 'SHIFT_G_OFF_X_PATH')))

# if __name__ == "__main__":
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
