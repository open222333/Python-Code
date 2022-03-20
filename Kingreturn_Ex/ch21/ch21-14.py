import pygal_maps_world.maps

worldMap = pygal_maps_world.maps.World()  # 建立世界圖物件
worldMap.title = 'China in the Map'  # 世界地圖標題
worldMap.add('China', ['cn'])  # 標記中國
worldMap.render_to_file('ch21/out21_14.svg')  # 儲存地圖檔案
