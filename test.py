from akad.ttypes import ApplicationType
import re
APP_TYPE = ApplicationType._VALUES_TO_NAMES[32]  # Android
APP_VER = '11.5.2'
CARRIER = '51089, 1-0'
SYSTEM_NAME = 'TOMTEST'
SYSTEM_VER = '11.5.2'
IP_ADDR = '8.8.8.8'
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
appName = '%s\t%s\t%s\t%s' % (
    APP_TYPE, APP_VER, SYSTEM_NAME, SYSTEM_VER)

print(appName)
