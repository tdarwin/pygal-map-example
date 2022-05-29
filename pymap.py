import pygal
from pygal.style import Style
from cairosvg import svg2png
from lxml import etree

custom_style = Style(
    background='#FFFFFF',
    plot_background='#FFFFFF',
    foreground='#FFFFFF',
    foreground_strong='#FFFFFF',  # Changes the colors of the lines between countries
    foreground_subtle='#FFFFFF',  # Changes the color of the lines between countries when emboldened
    colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'))  # Changes the color of the countries

# create a world map
worldmap = pygal.maps.world.SupranationalWorld(style=custom_style)

# set the title of map
# worldmap.title = 'Continents'

# Adding the continents to the mapping information
worldmap.add(None, 'africa')
worldmap.add(None, 'north_america')
worldmap.add(None, 'oceania')
worldmap.add(None, 'south_america')
worldmap.add(None, 'asia')
worldmap.add(None, 'europe')
worldmap.add(None, 'antartica')

# Render as an SVG file
worldmap.render_to_file('world.svg', width=6000, height=4600, dpi=1200)
print("rendered SVG")


# Process the map a bit for better presentation and fewer anomalies
tree = etree.parse(open("world.svg"))

# Removing all the desc tags, because we don't need them
desc_items = tree.xpath('//*[local-name()="svg"]//*[local-name()="g"]/*[local-name()="desc"]')
for x in desc_items:
    g = x.getparent()
    g.remove(x)

# Removing guam because it's mapped as a circle and looks weird
guam = tree.xpath('//*[local-name()="svg"]//*[local-name()="g"][contains(@class, "gu")]')[0]
g = guam.getparent()
g.remove(guam)

# Moving the weird bit of Russia between Latvia and Poland into the Latvia element so its color matches the rest of Europe
weird_russia = tree.xpath('//*[local-name()="svg"]//*[local-name()="g"]//*[local-name()="path"][contains(@d, "m1339.6")]')[0]
russia = weird_russia.getparent()
latvia = tree.xpath('//*[local-name()="svg"]//*[local-name()="g"][contains(@class, "lt")]')[0]
latvia.append(weird_russia)

# Moving the weird bit of Turkey to be part of Europe rather than Asia, so the map looks cleaner color-wise
weird_turkey = tree.xpath('//*[local-name()="svg"]//*[local-name()="g"]//*[local-name()="path"][contains(@d, "m1389.4")]')[0]
turkey = weird_turkey.getparent()
bulgaria = tree.xpath('//*[local-name()="svg"]//*[local-name()="g"][contains(@class, "bg")]')[0]
bulgaria.append(weird_turkey)

with open("world.svg", "wb") as o:
    o.write(etree.tostring(tree, pretty_print=True))

print("Modified SVG")

# Creating PNG file
svg2png(url='world.svg', write_to='world.png', dpi=1200, parent_width=6000, parent_height=4600, output_width=6000, output_height=4600)
print("Rendered PNG")

print("Success")
