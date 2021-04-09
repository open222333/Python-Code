import pygal_maps_world.maps
from pygal_maps_world.i18n import COUNTRIES

countrylist = list(COUNTRIES)
worldMap = pygal_maps_world.maps.World()
worldMap.title = 'World Language'
worldMap.add('ALL',countrylist)
worldMap.add('English-language system', ['en', 'us', 'ca', 'au', 'nz'])
worldMap.render_to_file('ch21/out21t_3.svg')
