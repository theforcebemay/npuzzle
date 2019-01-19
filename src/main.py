from Guard import Guard
from Input import Input

i = Input('maps/map.np')
g = Guard(i.get_content())
g.print_map()
