song = '''Are you sleeping, are you sleeping
Brother John, Brother John?
Morning bells are ringing
Morning bells are dinging
Ding-dang-dong, ding-dang-dong'''
song = song.lower()
song = song.replace(',', '')
song = song.replace('-', '')
song = song.replace('?', '')
song = song.replace('\n', ' ')
song_list = song.split(' ')
print(song)
print('song字數有%d' % len(song))
word = input('請輸入字串：')
print('%s此字串在song出現%d次' % (word, song.count(word)))
