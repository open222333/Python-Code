# 區域變數與全域變數使用相同的名稱
def printmsg():
    # 函數本身有定義變數,將執行列印區域變數功能
    msg = 'Local Variable'  # 設定區域變數
    print("函數列印：", msg)  # 列印區域變數


msg = 'Global Variable'  # 設定全域變數
print("主程式列印：", msg)  # 列印全域變數
printmsg()  # 呼叫函數
