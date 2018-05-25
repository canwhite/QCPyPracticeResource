#na_populations.py

import pygal.maps.world

wm = pygal.maps.world.World()
wm.title = "Populations of Countries in North America"
wm.add("North America",{"ca":24126000,"us":309349000,"mx":113423000})

wm.render_to_file("na_populations.svg")



