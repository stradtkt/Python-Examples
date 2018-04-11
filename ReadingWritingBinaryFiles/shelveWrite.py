import shelve 
# with shelve.open('ShelfTest') as fruit:
#   fruit['orange'] = "a sweet, orange, citrus fruit"
#   fruit['pear'] = "a sweet, pear, odd shaped apple"
#   fruit['apple'] = "a sweet, apple, good for your health"
#   fruit['grape'] = "a sweet, grape, sold in bunches"
#   fruit['lemon'] = "a sour, lemon, sour fruit"
#   print(fruit['lemon'])
#   print(fruit['grape'])

with shelve.open("bike") as bike:
  bike["make"] = "Honda"
  bike["model"] = "250 dream"
  bike["color"] = "red"
  bike["engine_size"] = 250

  print(bike["engine_size"])
  print(bike["color"])