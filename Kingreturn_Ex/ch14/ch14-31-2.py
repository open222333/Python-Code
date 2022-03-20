# 讀取(rb)和寫入(wb)二進位檔案 圖片 語音
src = 'ch14/01.png'
dst = 'ch14/011.png'
tmp = ''

with open(src, 'rb') as file_rd:
    tmp = file_rd.read()
    with open(dst, 'wb') as file_wr:
        file_wr.write(tmp)
