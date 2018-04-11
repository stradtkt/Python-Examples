menu = []
menu.append(["eggs", "bacon", "spam"])
menu.append(["eggs", "spam"])
menu.append(["eggs", "bacon", "sausage", "spam"])
menu.append(["eggs", "spam", "spam", "eggs"])
menu.append(["eggs", "bacon", "bread"])

print(menu)

for meal in menu:
  if not "spam" in meal:
    print(meal)
    for i in meal:
      print(i)