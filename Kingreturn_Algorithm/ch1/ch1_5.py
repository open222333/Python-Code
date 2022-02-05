from cProfile import label
from matplotlib import pyplot
import numpy

'''繪製 O(1) O(log n) O(n) O(nlog n) O(n**2)
n為1-10時 所需執行時間關係圖'''
n = numpy.linspace(1, 10, 10)  # 建立10個元素的陣列
ypt1 = n / n  # 時間複雜度是 O(1)
ypt2 = numpy.log2(n)  # 時間複雜度是 O(logn)
ypt3 = n  # 時間複雜度是 O(n)
ypt4 = n * numpy.log2(n)  # 時間複雜度是 O(nlogn)
ypt5 = n * n  # 時間複雜度是 O(n*n)
pyplot.plot(n, ypt1, "-o", label="O(1)")
pyplot.plot(n, ypt2, "-o", label="O(logn)")
pyplot.plot(n, ypt3, "-o", label="O(n)")
pyplot.plot(n, ypt4, "-o", label="O(nlogn)")
pyplot.plot(n, ypt5, "-o", label="O(n*n)")
pyplot.legend(loc="best")
pyplot.show()
