from PIL import Image, ImageDraw, ImageFont

newImage = Image.new('RGBA', (600, 300), 'Yellow')  # 建立600*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

strText = 'MingChi Institute of Technology'  # 設定欲列印英文字串
drawObj.text((50, 50), strText, fill='Blue')
# 使用古老英文字型，字型大小是36
fontInfo = ImageFont.truetype('/System/Library/Fonts/Apple Symbols.ttf', 36)
drawObj.text((50, 100), strText, fill='Blue', font=fontInfo)
# 處理中文字體
strCtext = '明志科技大學'  # 設定欲列印中文字串
fontInfo = ImageFont.truetype('/System/Library/Fonts/ヒラギノ明朝 ProN.ttc', 48)
drawObj.text((50, 180), strCtext, fill='Blue', font=fontInfo)
newImage.save('ch17/out17_22.png')
