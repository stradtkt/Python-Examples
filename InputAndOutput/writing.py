# cities = ["Cincinnati", "Frankfort", "Lexington", "Columbus", "Cleveland"]
# with open("cities.txt", 'w') as city_file:
#   for city in cities:
#     print(city, file=city_file)



# cities = []
# with open("cities.txt", 'r') as city_file:
#   for city in city_file:
#     cities.append(city.strip('\n'))
# print(cities)
# for city in cities:
#   print(city)

with open("sample.txt", 'a') as tables:
  for i in range(2,13):
    for j in range(1,13):
      print("{1:>2} times {0} is {2}".format(i, j, i * j), file=tables)
    print("-" * 20, file=tables)