# 隨機讀取二進位檔案 tell() seek(offset,origin)
dst = 'ch14/bdata'
bytedata = bytes(range(0, 256))
with open(dst, 'wb') as file_dst:
    file_dst.write(bytedata)
