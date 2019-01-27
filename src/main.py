from Guard import Guard
from Input import Input
from Map import Map

i = Input('maps/map.np')
g = Guard(i.get_content())
g.read_map()
map_, size = g.get_map
m = Map(size, map_)
print(type(m))
m.map = m.generate_map(0)
print(type(m))
m.get_final_state()
