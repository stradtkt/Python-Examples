# def python_food():
#   width = 80
#   text = "Spam and eggs"
#   left_margin = (width - len(text)) // 2
#   print(" " * left_margin, text)

def center_text(*args, sep=' '):
  text = ""
  for arg in args:
    text += str(arg) + sep
  left_margin = (80 - len(text)) // 2
  return " " * left_margin + text

# with open("centered", mode='w') as center_file:
#   center_text("Spam and eggs", file=center_file)
#   center_text("Hello world", file=center_file)
#   center_text("My name is Kevin", file=center_file)
#   center_text(28, file=center_file)
#   center_text("first", "second", 3, 4, "spam", sep=":", file=center_file)

print(center_text("Spam and eggs"))
print(center_text("Hello world"))
print(center_text("My name is Kevin"))
print(center_text(28))
print(center_text("first", "second", 3, 4, "spam", sep=":"))
print("=" + str(12*3))
print(sorted(["b", "d", "c", "a"]))