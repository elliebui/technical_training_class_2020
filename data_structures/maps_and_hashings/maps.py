# udacity = {}
# udacity['u'] = 1
# udacity['d'] = 2
# udacity['a'] = 3
# udacity['c'] = 4
# udacity['i'] = 5
# udacity['t'] = 6
# udacity['y'] = 7
#
# print (udacity)
# # {'u': 1, 'd': 2, 'a': 3, 'c': 4, 'i': 5, 't': 6, 'y': 7}
#
# print (udacity['t'])
# # 6


# dictionary = {}
# dictionary['d'] = [1]
# dictionary['i'] = [2]
# dictionary['c'] = [3]
# dictionary['t'] = [4]
# dictionary['i'].append(5)
# dictionary['o'] = [6]
# dictionary['n'] = [7]
# dictionary['a'] = [8]
# dictionary['r'] = [9]
# dictionary['y'] = [10]
# print (dictionary)
# # {'d': [1], 'i': [2, 5], 'c': [3], 't': [4], 'o': [6], 'n': [7], 'a': [8], 'r': [9], 'y':[10]}

# Cities to add:
# Bangalore (India, Asia)
# Atlanta (USA, North America)
# Cairo (Egypt, Africa)
# Shanghai (China, Asia)

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

print(locations)


# Print a list of all cities in the USA in alphabetic order.
for city in sorted(locations['North America']['USA']):
    print(city)


# Print all cities in Asia, in alphabetic order, next to the name of the country

cities = [locations['Asia'][item] for item in locations['Asia']]
asia_city_list = list()

for asia_country, asia_cities in locations['Asia'].items():
    city_country = asia_cities[0] + " - " + asia_country
    asia_city_list.append(city_country)

for city in sorted(asia_city_list):
    print(city)

