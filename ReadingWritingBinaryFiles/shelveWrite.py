import shelve 
# with shelve.open('ShelfTest') as fruit:
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['pear'] = "a sweet, pear, odd shaped apple"
# fruit['apple'] = "a sweet, apple, good for your health"
# fruit['grape'] = "a sweet, grape, sold in bunches"
# fruit['lemon'] = "a sour, lemon, sour fruit"
#   print(fruit['lemon'])
#   print(fruit['grape'])

# with shelve.open("bike") as bike:
#   bike["make"] = "Honda"
#   bike["model"] = "250 dream"
#   bike["color"] = "red"
#   bike["engine_size"] = 250
#   print(bike["engine_size"])
#   print(bike["color"])

# fruit = shelve.open('ShelfTest')
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['pear'] = "a sweet, pear, odd shaped apple"
# fruit['apple'] = "a sweet, apple, good for your health"
# fruit['grape'] = "a sweet, grape, sold in bunches"
# fruit['lemon'] = "a sour, lemon, sour fruit"
# while True:
#   dict_key = input("Please enter a fruit: ")
#   if dict_key == "quit":
#     break
#   if dict_key in fruit:
#     description = fruit[dict_key]
#     print(description)
#   else: 
#     print("We do not have a "+ dict_key)
# fruit.close()