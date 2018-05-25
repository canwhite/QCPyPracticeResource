#countries.py

from pygal.maps.world import COUNTRIES 

for country_code in sorted(COUNTRIES.keys()):
	print(country_code,COUNTRIES,COUNTRIES[country_code])






