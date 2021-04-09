# 呼叫函數時參數是串列 基本傳遞串列參數的應用
def product_msg(customers):
    str1 = '親爱的'
    str2 = '本公司將在2020年12月20日北京舉行產品發表會'
    str3 = '總經理:深石敬上'
    for customer in customers:
        msg = str1 + customer + '\n' + str2 + '\n' + str3
        print(msg, '\n')


members = ['Damon', 'Peter', 'Mary']
product_msg(members)
