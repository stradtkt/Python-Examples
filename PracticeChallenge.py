ipAddress = input("Please enter your IP address: ")

segment = 1
segment_length = 0
character = '' # will have a value if it runs without a IP address entered

for character in ipAddress:
  if character == '.':
    print("segment {} contains {} characters".format(segment, segment_length))
    segment += 1
    segment_length = 0
  else:
    segment_length += 1
#unless the final  character in the string was a . then we haven't printed the last segment
if character != '.':
  print("segment {} contains {} charcters".format(segment, segment_length))
