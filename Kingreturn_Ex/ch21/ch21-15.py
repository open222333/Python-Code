import pygal_maps_world.maps as pm

worldMap = pm.World()  # 建立世界地圖物件
worldMap.title = 'China/Japan/Thailand'  # 世界地圖標題
worldMap.add('Asia', ['cn', 'jp', 'th'])  # 標記Asia
worldMap.render_to_file('ch21/out21_15.svg')
