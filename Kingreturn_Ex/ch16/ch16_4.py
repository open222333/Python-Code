# re模組 findall()方法
import re

msg1 = " Please call my secretary using 0930-919-919 or 0952-001-001"
msg2 = "請明天17:30和我一起參加明志科大教師節晚餐"
msg3 = "請明天17:30和我一起參加明志科大教師節晚餐,可用0933-080-080聯絡我"


def parseString(string):
    """解析字串是否含有電話號碼"""
    phoneRule = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
    phoneNum = phoneRule.findall(string)  # 使用串列傳回搜尋結果
    print("電話號碼是：%s" % phoneNum)  # 串列方式顯示電話號碼


parseString(msg1)
parseString(msg2)
parseString(msg3)
