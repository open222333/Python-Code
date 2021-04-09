def modifySong(songStr):  # 將標點符號用空白字元取代
    for ch in songStr:
        if ch in '.,?':
            songStr = songStr.replace(ch, '')
    return songStr


def wordCount(songCount):
    songList = songCount.split()
    mydict = {wd: songList.count(wd) for wd in set(songList)}
    return mydict


fn = 'ch14/ch14_51.txt'
with open(fn) as file_Obj:
    song = file_Obj.read()

song = modifySong(song.lower())
song = wordCount(song)
newsonglist = sorted(song.items(), key=lambda item: item[1], reverse=True)
for wd, count in newsonglist:
    print(wd, count)
