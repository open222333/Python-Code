# 專題 傳統方式分析文章的文字與字數
song = """Are you sleeping, are you sleeping
Brother John, Brother John?
Morning bells are ringing
Morning bells are dinging
Ding-dang-dong, ding-dang-dong"""
mydict = {}  # 空字典未來儲存單字計數結果
print("原始歌曲")
print(song)

# 以下是將歌曲大寫字母全部改成小寫
songLower = song.lower()  # 歌曲改為小寫

# 將歌曲的標點符號用空字元取代
for ch in songLower:
    if ch in '.,?-':
        songLower = songLower.replace(ch, ' ')

# 將歌曲字串轉成串列
songList = songLower.split()
# 將歌曲串列處理成字典
for wd in songList:
    if wd in mydict:  # 檢查此字是否已在字典內
        mydict[wd] += 1  # 累計出現次數
    else:
        mydict[wd] = 1  # 第一次出現的字建立此鍵與值
print("以下是最後執行結果")
print(mydict)  # 列印字典
print("出現最多出現的單字：", max(mydict.items(), key=lambda i: i[1]))
