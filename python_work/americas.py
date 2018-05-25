#americas.py
import pygal.maps.world

vm = pygal.maps.world.World()
vm.title = "Populations of Countries in North America"
vm.add("North America",["ca","mx","us"])
vm.add("Center America",["bz","cr","gt","hn","ni","pa","sv"])
vm.add("South America",["ar","bo","br","cl","co","ec","gf","gy","pe","py","sr","uy","ve"])


vm.render_to_file("americas.svg")




