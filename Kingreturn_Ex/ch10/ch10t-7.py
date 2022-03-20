# 專題 雞尾酒
cocktail = {'Blue Hawaiian': {'Rum', 'Sweet Wine', 'Cream', 'Pineapple Juice', 'Lemon Juice'},
            'Ginger Mojito': {'Rum', 'Ginger', 'Mint Leaves', 'Lime Juice', 'Ginger Soda'},
            'New Yorker': {'Whiskey', 'Red Wine', 'Lemon Juice', 'Sugar Syrup'},
            'Bloody Mary': {'Vodka', 'Lemon Juice', 'Tomato Juice', 'Tabasco', 'Little Sale'},
            'Horse\'s Neck': {'Brandy', 'Ginger Soda'},
            'Cosmopolitan': {'Vodka', 'Sweet Wine', 'Lime Juice', 'Cranberry Juice'},
            'Sex on the Beach': {'Vodka', 'Peach Liqueur', 'Orange Juice', 'Cranberry Juice'}}
# 列出含有Vodka的酒
print("含有Vodka的酒：")
for name, formulas, in cocktail.items():
    if 'Vodka' in formulas:
        print(name)
# 列出含有Sweet Wine的酒
print("含有Sweet Wine的酒：")
for name, formulas in cocktail.items():
    if 'Sweet Wine' in formulas:
        print(name)
# 列出含有Vodka和Cranberry Juice的酒
print("含有Vodka和Cranberry Juice的酒：")
for name, formulas in cocktail.items():
    if 'Vodka' in formulas and 'Cranberry Juice' in formulas:
        print(name)
# 列出含有Vodka但是沒有Cranberry Juice的酒
print("含有Vodka但是沒有Cranberry Juice的酒：")
for name, formulas in cocktail.items():
    if 'Lemon Juice' in formulas and not ('Cranberry Juice' in formulas):
        print(name)
