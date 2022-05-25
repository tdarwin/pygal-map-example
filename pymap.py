import pygal
from pygal.style import Style

custom_style = Style(
    background='#FFFFFF',
    plot_background='transparent',
    foreground='#53E89B',
    foreground_strong='#53A0E8',
    foreground_subtle='#630C0D',
    opacity='.6',
    opacity_hover='.9',
    transition='400ms ease-in',
    colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'))

# create a world map
worldmap = pygal.maps.world.SupranationalWorld(style=custom_style)

# set the title of map
worldmap.title = 'Continents'

# adding the continents
worldmap.add('Africa', [('africa')])
worldmap.add('North america', [('north_america')])
worldmap.add('Oceania', [('oceania')])
worldmap.add('South america', [('south_america')])
worldmap.add('Asia', [('asia')])
worldmap.add('Europe', [('europe')])
worldmap.add('Antartica', [('antartica')])

# save into the file
worldmap.render_to_png('world.png')

print("Success")
