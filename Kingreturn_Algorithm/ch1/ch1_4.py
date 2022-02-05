from cProfile import label
from pickletools import pylist
from matplotlib.pyplot import plot
from matplotlib import pyplot
import numpy

'''時間複雜度'''
xpt = numpy.linspace(1, 10, 10)  # 建立含10個元素的陣列
ypt1 = xpt / xpt  # 時間複雜度是 O(1)
ypt2 = numpy.log2(xpt)  # 時間複雜度是O(logn)
ypt3 = xpt  # 時間複雜度是O(n)
plot(xpt, ypt1, "-o", label="O(1)")
plot(xpt, ypt2, "-o", label="O(logn)")
plot(xpt, ypt3, "-o", label="O(n)")
pyplot.legend(loc="best")  # 建立圖例
pyplot.show()
