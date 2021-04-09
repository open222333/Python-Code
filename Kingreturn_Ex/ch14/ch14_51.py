# 專題 以讀取檔案方式處理分析檔案
def modifySong(songStr):  # 將歌曲的標點符號用空字元取代
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch, '')
    return songStr


def wordCount(songCount):
    global mydict
    songList = songCount.split()  # 將歌曲字串轉成串列
    print("以下是歌曲串列")
    print(songList)
    # 鍵 為 wd 值為 songList.count(wd)
    mydict = {wd: songList.count(wd) for wd in set(songList)}


fn = 'ch14/ch14_51.txt'
with open(fn) as file_Obj:  # 開啟歌曲檔案
    data = file_Obj.read()  # 讀取歌曲檔案
    print("以下是所讀取的檔案")
    print("data")  # 列印歌曲檔案

mydict = []  # 空字典以未來儲存單字計數結果
print("以下是將歌曲大寫字母全部改成小寫同時將標點符號用空字元取代")
song = modifySong(data.lower())
print(song)

wordCount(song)  # 執行歌曲單字計數
print("以下是最後執行結果")
print(mydict)  # 列印字典
