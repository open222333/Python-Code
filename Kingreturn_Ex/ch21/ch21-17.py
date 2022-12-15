# 讓地圖呈現數據
import pygal_maps_world.maps

worldMap = pygal_maps_world.maps.World()  # 建立世界地圖物件
worldMap.title = 'Populations in China/Japan/Thailand'  # 世界地圖標題
worldMap.add('Asia', {'cn': 1262645000,
                      'jp': 126870000, 'th': 63155029})  # 標記人口資訊
worldMap.render_to_file('ch21/out21_17.svg')  # 儲存地圖檔案
