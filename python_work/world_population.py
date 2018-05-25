#world_population.py
#将数据加载在一个列表里
import json
import pygal.maps.world
from pygal.style import RotateStyle
from country_codes import get_country_code
filename = "population_data.json"


#将数据加载到列表中
with open(filename) as f:
	pop_data = json.load(f)


#打印每个国家2010年的人口数量
#创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
	if pop_dict["Year"] == "2010":
		country_name = pop_dict["Country Name"]
		#将字符串转化为数字
		population = int(float(pop_dict["Value"]))
		code = get_country_code(country_name)
		if code:
			cc_populations[code] = population
		else:
			print("ERROR-"+country_name)

#根据人口数量，将所有的国家分组
cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}
for cc,pop in cc_populations.items():
	if pop <10000000:
		cc_pops_1[cc] = pop
	elif pop < 1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop

print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

		
wm = pygal.maps.world.World()
wm_style = RotateStyle("#336699")
wm = pygal.maps.world.World(style = wm_style)

wm.title = "World Population in 2010, by Country"
wm.add('0-10m',cc_pops_1)
wm.add("10m-1bn",cc_pops_2)
wm.add(">1bn",cc_pops_3)

wm.render_to_file("world_population.svg")




