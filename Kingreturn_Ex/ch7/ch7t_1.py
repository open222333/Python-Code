files_list = ['da1.jpg', 'da2.png', 'da3,gif',
              'da4.gif', 'da5.jpg', 'da6.jpg', 'da7.gif']
jpg_list = []
png_list = []
gif_list = []
for file in files_list:
    if file.endswith('.jpg'):
        jpg_list.append(file)
    elif file.endswith('.png'):
        png_list.append(file)
    elif file.endswith('.gif'):
        gif_list.append(file)
    else:
        continue
print('JPG:', jpg_list, '\nPNG:', png_list, '\nGIF:', gif_list)
