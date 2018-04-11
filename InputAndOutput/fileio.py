# jabber = open("C:/Users/Kevin/source/repos/PracticePY/PracticePY/InputAndOutput/sample.txt", 'r')

# for line in jabber:
#   if "jabberwock" in line.lower():
#     print(line, end='')

# jabber.close()

# with open("C:/Users/Kevin/source/repos/PracticePY/PracticePY/InputAndOutput/sample.txt", 'r') as jabber:
#   for line in jabber:
#     if "JAB" in line.upper():
#       print(line, end='')

with open("C:/Users/Kevin/source/repos/PracticePY/PracticePY/InputAndOutput/sample.txt", 'r') as jabber:
  lines = jabber.readlines()
print(lines)

with open("C:/Users/Kevin/source/repos/PracticePY/PracticePY/InputAndOutput/sample.txt", 'r') as jabber:
  lines = jabber.read()
print(lines)