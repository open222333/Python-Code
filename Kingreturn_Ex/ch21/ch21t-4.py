import pygal_maps_world.maps as pmwm

worldMap = pmwm.World()
worldMap.add('Asia', {'cn': 1262645000, 'jp': 126870000, 'th': 63155029})
worldMap.add('Europe', {'fn': 60762406, 'se': 11011781})
worldMap.add('Africa', {'za': 44000833})
worldMap.render_to_file('ch21/out21t_4.svg')
