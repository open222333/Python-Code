#  is 和 is not 運算式 應用在串列變數
mysports = ['basketball', 'baseball']
sports1 = mysports  # 賦值
sports2 = mysports[:]  # 切片拷貝新串列
print("我喜歡的運動 ＝ ", mysports, "位址是 ＝ ", id(mysports))
print("運動1 ＝ ", sports1, "位址是 ＝ ", id(sports1))
print("運動2 ＝ ", sports2, "位址是 ＝ ", id(sports2))
boolean_value = mysports is sports1
print("我喜歡的運動 is 運動 1 ＝ ", boolean_value)

boolean_value = mysports is sports2
print("我喜歡的運動 is 運動 2 ＝ ", boolean_value)

boolean_value = mysports is not sports1
print("我喜歡的運動 is 運動 1 ＝ ", boolean_value)

boolean_value = mysports is not sports2
print("我喜歡的運動 is 運動 2 ＝ ", boolean_value)
